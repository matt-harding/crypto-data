from models.StableCoin import StableCoin
from pycoingecko import CoinGeckoAPI
from coinmarketcapapi import CoinMarketCapAPI
from coinmetrics.api_client import CoinMetricsClient
from messari.messari import Messari
from datetime import datetime, timedelta
import requests

QUOTE_CURRENCY = 'usd'
COINMARKETCAP_API_KEY = '1fb4a911-50e9-4685-bd6c-5182699bbb86'
CRYPTOCOMPARE_API_KEY = 'bafc411354db9bb7ea7b67f06ca4fb1d485169fb5c54d860e236b7116f0a2094'

def fetch_data_from_coin_gecko(coin_ids: list) -> list:
    """Fetches the data from CoinGecko API and returns it as a list of StableCoin objects"""
    coins = []
    try:
        cg = CoinGeckoAPI()

        market_data = cg.get_coins_markets(vs_currency=QUOTE_CURRENCY)

        for coin_data in market_data:
            if coin_data['id'] in coin_ids:
                coin = StableCoin()
                coin.id = coin_data['id']
                coin.symbol = coin_data['symbol']
                coin.name = coin_data['name']
                coin.market_cap = coin_data['market_cap']
                coin.circulating_supply = coin_data['circulating_supply']
                coin.total_supply = coin_data['total_supply']
                coin.twentyfourhour_volume = coin_data['total_volume']
                coin.price = coin_data['current_price']
                coin.last_updated = coin_data['last_updated']

                coins.append(coin)
    except Exception as e:
        print(e)

    return coins

def fetch_data_from_coin_market_cap(coin_ids: list) -> list:
    """Fetches the data from CoinMarketCap API and returns it as a list of StableCoin objects"""
    coins = []
    try:
        cmc = CoinMarketCapAPI(COINMARKETCAP_API_KEY)

        rep = cmc.cryptocurrency_listings_latest()

        coins = []
        
        for coin_data in rep.data:
            if coin_data['symbol'] in coin_ids:
                coin = StableCoin()
                coin.id = coin_data['id']
                coin.symbol = coin_data['symbol']
                coin.name = coin_data['name']
                coin.market_cap = coin_data['quote']['USD']['market_cap']
                coin.circulating_supply = coin_data['circulating_supply']
                coin.total_supply = coin_data['total_supply']
                coin.twentyfourhour_volume = coin_data['quote']['USD']['volume_24h']
                coin.price = coin_data['quote']['USD']['price']
                coin.last_updated = coin_data['last_updated']

                coins.append(coin)

    except Exception as e:
        print(e)

    return coins

def fetch_data_from_coin_metrics(coin_ids: list) -> list:
    """Fetches the data from CoinMetrics API and returns it as a list of StableCoin objects"""
    coins = []
    try:
        client = CoinMetricsClient()
        metrics = ['CapMrktCurUSD', 'SplyActEver', 'SplyCur', 'PriceUSD']

        asset_metrics = client.get_asset_metrics(
            assets=coin_ids,
            metrics=metrics,
            start_time=(
                datetime.today() -
                timedelta(
                    days=1)).strftime('%Y-%m-%d'),
            end_time=datetime.today().strftime('%Y-%m-%d'))

        for coin_data in asset_metrics:
            coin = StableCoin()
            coin.symbol = coin_data['asset']
            coin.market_cap = coin_data['CapMrktCurUSD']
            coin.price = coin_data['PriceUSD']
            coin.circulating_supply = coin_data['SplyCur']
            coin.total_supply = coin_data['SplyActEver']
            coins.append(coin)

    except Exception as e:
        print(e)

    return coins

def fetch_data_from_crypto_compare(coin_ids: list) -> list:
    """Fetches the data from CryptoCompare API and returns it as a list of StableCoin objects"""
    coins = []

    try:
        url = "https://min-api.cryptocompare.com/data/pricemultifull"

        querystring = {"fsyms":','.join(coin_ids),"tsyms":'usd',"api_key":CRYPTOCOMPARE_API_KEY}

        response = requests.request("GET", url, params=querystring)

        data = response.json()

        for coin_symbol in coin_ids:
            stablecoin = StableCoin()
            stablecoin.id = data['RAW'][coin_symbol]['USD']['FROMSYMBOL']
            stablecoin.symbol = data['RAW'][coin_symbol]['USD']['FROMSYMBOL']
            stablecoin.market_cap = data['RAW'][coin_symbol]['USD']['MKTCAP']
            stablecoin.circulating_supply = data['RAW'][coin_symbol]['USD']['CIRCULATINGSUPPLY']
            stablecoin.total_supply = data['RAW'][coin_symbol]['USD']['SUPPLY']
            stablecoin.twentyfourhour_volume = data['RAW'][coin_symbol]['USD']['TOTALVOLUME24H']
            stablecoin.price = data['RAW'][coin_symbol]['USD']['PRICE']
            stablecoin.last_updated = data['RAW'][coin_symbol]['USD']['LASTUPDATE']
            coins.append(stablecoin)

    except Exception as e:
        print(e)
    
    return coins

def fetch_data_from_on_chain_fx(coin_ids: list) -> list:
    """Fetches the data from OnChainFX API and returns it as a list of StableCoin objects"""
    coins = []

    try:
        messari = Messari()

        asset_metric_df = messari.get_asset_metrics(asset_slugs=coin_ids)

        coins = []
        for asset in coin_ids:
            coin = StableCoin()
            coin.id = asset
            coins.append(coin)

        for coin in coins:
            coin.symbol = asset_metric_df['symbol'][coin.id]
            coin.name = asset_metric_df['name'][coin.id]
            coin.price = asset_metric_df['market_data_price_usd'][coin.id]
            coin.market_cap = asset_metric_df['marketcap_current_marketcap_usd'][coin.id]
            coin.circulating_supply = asset_metric_df['supply_circulating'][coin.id]
            # No other supply metrics return values
            coin.total_supply = 0
            # Note there is also prop 'market_data_real_volume_last_24_hours'
            coin.twentyfourhour_volume = asset_metric_df['market_data_volume_last_24_hours'][coin.id]
            coin.price = asset_metric_df['market_data_price_usd'][coin.id]

    except Exception as e:
        print(e)
    
    return coins


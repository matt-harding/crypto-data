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


def fetch_data_from_coin_gecko(target_coins: dict) -> list:
    """Fetches the data from CoinGecko API and returns it as a list of StableCoin objects"""
    try:
        cg = CoinGeckoAPI()

        market_data = cg.get_coins_markets(vs_currency=QUOTE_CURRENCY)

        for coin_data in market_data:
            if coin_data['id'] in target_coins.keys():
                target_coins[coin_data['id']].data_provider = 'CoinGecko'
                target_coins[coin_data['id']].market_cap = coin_data['market_cap']
                target_coins[coin_data['id']].circulating_supply = coin_data['circulating_supply']
                target_coins[coin_data['id']].total_supply = coin_data['total_supply']
                target_coins[coin_data['id']].twentyfourhour_volume = coin_data['total_volume']
                target_coins[coin_data['id']].price = coin_data['current_price']
                target_coins[coin_data['id']].last_updated = coin_data['last_updated']

    except Exception as e:
        print(e)

    return target_coins.values()


def fetch_data_from_coin_market_cap(target_coins: dict) -> list:
    """Fetches the data from CoinMarketCap API and returns it as a list of StableCoin objects"""
    try:
        cmc = CoinMarketCapAPI(COINMARKETCAP_API_KEY)

        rep = cmc.cryptocurrency_listings_latest()

        for coin_data in rep.data:
            if coin_data['symbol'] in target_coins.keys():
                target_coins[coin_data['symbol']].data_provider = 'CoinMarketCap'
                target_coins[coin_data['symbol']].market_cap = coin_data['quote']['USD']['market_cap']
                target_coins[coin_data['symbol']].circulating_supply = coin_data['circulating_supply']
                target_coins[coin_data['symbol']].total_supply = coin_data['total_supply']
                target_coins[coin_data['symbol']].twentyfourhour_volume = coin_data['quote']['USD']['volume_24h']
                target_coins[coin_data['symbol']].price = coin_data['quote']['USD']['price']
                target_coins[coin_data['symbol']].last_updated = coin_data['last_updated']

    except Exception as e:
        print(e)

    return target_coins.values()


def fetch_data_from_coin_metrics(target_coins: dict) -> list:
    """Fetches the data from CoinMetrics API and returns it as a list of StableCoin objects"""
    try:
        client = CoinMetricsClient()
        metrics = ['CapMrktCurUSD', 'SplyActEver', 'SplyCur', 'PriceUSD']
        asset_metrics = client.get_asset_metrics(
            assets=list(target_coins.keys()),
            metrics=metrics,
            start_time=(
                datetime.today() -
                timedelta(
                    days=1)).strftime('%Y-%m-%d'),
            end_time=datetime.today().strftime('%Y-%m-%d'))
        
        for coin_data in asset_metrics:
            if coin_data['asset'] in list(target_coins.keys()):
                target_coins[coin_data['asset']].data_provider = 'CoinMetrics'
                target_coins[coin_data['asset']].market_cap = float(coin_data['CapMrktCurUSD'])
                target_coins[coin_data['asset']].circulating_supply = float(coin_data['SplyCur'])
                target_coins[coin_data['asset']].total_supply = float(coin_data['SplyActEver'])
                target_coins[coin_data['asset']].price = float(coin_data['PriceUSD'])


    except Exception as e:
        print(e)

    return target_coins.values()


def fetch_data_from_crypto_compare(target_coins: dict) -> list:
    """Fetches the data from CryptoCompare API and returns it as a list of StableCoin objects"""
    try:
        url = "https://min-api.cryptocompare.com/data/pricemultifull"

        querystring = {
            "fsyms": ','.join(target_coins.keys()),
            "tsyms": 'usd',
            "api_key": CRYPTOCOMPARE_API_KEY}

        response = requests.request("GET", url, params=querystring)

        data = response.json()

        for coin_symbol in target_coins.keys():
            target_coins[coin_symbol].data_provider = 'CryptoCompare'
            target_coins[coin_symbol].market_cap = data['RAW'][coin_symbol]['USD']['MKTCAP']
            target_coins[coin_symbol].circulating_supply = data['RAW'][coin_symbol]['USD']['CIRCULATINGSUPPLY']
            target_coins[coin_symbol].total_supply = data['RAW'][coin_symbol]['USD']['SUPPLY']
            target_coins[coin_symbol].twentyfourhour_volume = data['RAW'][coin_symbol]['USD']['TOTALVOLUME24H']
            target_coins[coin_symbol].price = data['RAW'][coin_symbol]['USD']['PRICE']
            target_coins[coin_symbol].last_updated = datetime.utcfromtimestamp(int(data['RAW'][coin_symbol]['USD']['LASTUPDATE'])).strftime('%Y-%m-%d %H:%M:%S')

    except Exception as e:
        print(e)

    return target_coins.values()


def fetch_data_from_on_chain_fx(target_coins: dict) -> list:
    """Fetches the data from OnChainFX API and returns it as a list of StableCoin objects"""
    try:
        messari = Messari()

        asset_metric_df = messari.get_asset_metrics(asset_slugs=list(target_coins.keys()))

        for coin_id in list(target_coins.keys()):
            target_coins[coin_id].price = asset_metric_df['market_data_price_usd'][coin_id]
            target_coins[coin_id].market_cap = asset_metric_df['marketcap_current_marketcap_usd'][coin_id]
            target_coins[coin_id].circulating_supply = asset_metric_df['supply_circulating'][coin_id]
            # # No other supply metrics return values
            # target_coins[coin_id].total_supply = 'N/A'
            # Note there is also prop 'market_data_real_volume_last_24_hours'
            target_coins[coin_id].twentyfourhour_volume = asset_metric_df['market_data_volume_last_24_hours'][coin_id]

    except Exception as e:
        print(e)

    return target_coins.values()

import pandas as pd
from models.StableCoin import StableCoin
from utils.data_providers import fetch_data_from_coin_gecko, fetch_data_from_coin_market_cap, fetch_data_from_coin_metrics, fetch_data_from_crypto_compare, fetch_data_from_on_chain_fx

TARGET_DATA_PROVIDERS = [
    'CoinGecko',
    'CoinMarketCap',
    #'CoinMetrics',
    'CryptoCompare',
    'OnChainFX'
]

def get_coin_ids(exchange_name: str) -> list:
    # switch statement for different exchanges
    if exchange_name == 'CoinGecko':
        return {
            'tether': StableCoin(symbol='USDT', name='Tether', data_provider='CoinGecko'),
            'usd-coin': StableCoin(symbol='USDC', name='USD Coin', data_provider='CoinGecko'),
            'binance-usd': StableCoin(symbol='BUSD', name='Binance USD', data_provider='CoinGecko'),
            'dai': StableCoin(symbol='DAI', name='Dai', data_provider='CoinGecko'),
            'frax': StableCoin(symbol='FRAX', name='FRAX', data_provider='CoinGecko'),
            'paxos-standard': StableCoin(symbol='USDP', name='Pax Dollar', data_provider='CoinGecko'),
            'gemini-dollar': StableCoin(symbol='GUSD', name='Gemini Dollar', data_provider='CoinGecko'),
            'true-usd': StableCoin(symbol='TUSD', name='TrueUSD', data_provider='CoinGecko'),
        }
    elif exchange_name == 'CoinMarketCap':
        return {
            'USDT': StableCoin(symbol='USDT', name='Tether', data_provider='CoinMarketCap'),
            'USDC': StableCoin(symbol='USDC', name='USD Coin', data_provider='CoinMarketCap'),
            'BUSD': StableCoin(symbol='BUSD', name='Binance USD', data_provider='CoinMarketCap'),
            'DAI': StableCoin(symbol='DAI', name='Dai', data_provider='CoinMarketCap'),
            'USDP': StableCoin(symbol='USDP', name='Pax Dollar', data_provider='CoinMarketCap'),
            'GUSD': StableCoin(symbol='GUSD', name='Gemini Dollar', data_provider='CoinMarketCap'),
            'TUSD': StableCoin(symbol='TUSD', name='TrueUSD', data_provider='CoinMarketCap'),
        }
    elif exchange_name == 'CoinMetrics':
        return {
            'usdt': StableCoin(symbol='USDT', name='Tether', data_provider='CoinMetrics'),
            'usdc': StableCoin(symbol='USDC', name='USD Coin', data_provider='CoinMetrics'),
            'busd': StableCoin(symbol='BUSD', name='Binance USD', data_provider='CoinMetrics'),
            'dai': StableCoin(symbol='DAI', name='Dai', data_provider='CoinMetrics'),
            'frax': StableCoin(symbol='FRAX', name='FRAX', data_provider='CoinMetrics'),
            'gusd': StableCoin(symbol='GUSD', name='Gemini Dollar', data_provider='CoinMetrics'),
            'tusd': StableCoin(symbol='TUSD', name='TrueUSD', data_provider='CoinMetrics'),
        }
    elif exchange_name == 'CryptoCompare':
        return {
            'USDT': StableCoin(symbol='USDT', name='Tether', data_provider='CryptoCompare'),
            'USDC': StableCoin(symbol='USDC', name='USD Coin', data_provider='CryptoCompare'),
            'BUSD': StableCoin(symbol='BUSD', name='Binance USD', data_provider='CryptoCompare'),
            'DAI': StableCoin(symbol='DAI', name='Dai', data_provider='CryptoCompare'),
            'USDP': StableCoin(symbol='USDP', name='Pax Dollar', data_provider='CryptoCompare'),
            'FRAX': StableCoin(symbol='FRAX', name='FRAX', data_provider='CryptoCompare'),
            'GUSD': StableCoin(symbol='GUSD', name='Gemini Dollar', data_provider='CryptoCompare'),
            'TUSD': StableCoin(symbol='TUSD', name='TrueUSD', data_provider='CryptoCompare'),
        }
    elif exchange_name == 'OnChainFX':
        return {
            'tether': StableCoin(symbol='USDT', name='Tether', data_provider='OnChainFX'),
            'usd-coin': StableCoin(symbol='USDC', name='USD Coin', data_provider='OnChainFX'),
            'binance-usd': StableCoin(symbol='BUSD', name='Binance USD', data_provider='OnChainFX'),
            'dai': StableCoin(symbol='DAI', name='Dai', data_provider='OnChainFX'),
            'pax-dollar': StableCoin(symbol='USDP', name='Pax Dollar', data_provider='OnChainFX'),
            'frax': StableCoin(symbol='FRAX', name='FRAX', data_provider='OnChainFX'),
            'gemini-dollar': StableCoin(symbol='GUSD', name='Gemini Dollar', data_provider='OnChainFX'),
            'tusd': StableCoin(symbol='TUSD', name='TrueUSD', data_provider='OnChainFX'),
        }


def get_coin_data(exchange_name: str) -> list:
    """Fetches the data from the exchange and returns it as a list of StableCoin objects"""
    coin_ids = get_coin_ids(exchange_name)
    if exchange_name == 'CoinGecko':
        return fetch_data_from_coin_gecko(coin_ids)
    elif exchange_name == 'CoinMarketCap':
        return fetch_data_from_coin_market_cap(coin_ids)
    elif exchange_name == 'CoinMetrics':
        return fetch_data_from_coin_metrics(coin_ids)
    elif exchange_name == 'CryptoCompare':
        return fetch_data_from_crypto_compare(coin_ids)
    elif exchange_name == 'OnChainFX':
        return fetch_data_from_on_chain_fx(coin_ids)

# python main function
if __name__ == '__main__':
    all_data = []
    for data_provider in TARGET_DATA_PROVIDERS:
        print(f"Fetching data from {data_provider}")
        coins = get_coin_data(data_provider)
        all_data.extend(coins)

    df = pd.DataFrame(all_data)
    print('Fetch finised') 
    print(df)

    # export df to excel
    df.to_excel('stablecoins.xlsx')

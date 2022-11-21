import pandas as pd
from utils.data_providers import fetch_data_from_coin_gecko, fetch_data_from_coin_market_cap, fetch_data_from_coin_metrics, fetch_data_from_crypto_compare, fetch_data_from_on_chain_fx

TARGET_DATA_PROVIDERS = [
    'CoinGecko',
    'CoinMarketCap',
    'CoinMetrics',
    'CryptoCompare',
    'OnChainFX']


def get_coin_ids(exchange_name: str) -> list:
    # switch statement for different exchanges
    if exchange_name == 'CoinGecko':
        return [
            'tether',
            'usd-coin',
            'binance-usd',
            'dai',
            #'usdp',
            'gemini-dollar',
            'true-usd']
    elif exchange_name == 'CoinMarketCap':
        # need to check if 'usdp' is not on CMC
        target_coin_symbols = ['usdt', 'usdc', 'busd', 'dai', 'tusd', 'gusd']
        target_coin_symbols = [symbol.upper()
                               for symbol in target_coin_symbols]
        return target_coin_symbols
    elif exchange_name == 'CoinMetrics':
        # need to check if 'usdp' is not on CoinMetrics
        return ['usdt', 'usdc', 'busd', 'dai', 'tusd', 'gusd']
    elif exchange_name == 'CryptoCompare':
        # need to check if 'usdp' is not on CryptoCompare
        return ['TUSD', 'USDC', 'BUSD', 'DAI', 'TUSD', 'GUSD']
    elif exchange_name == 'OnChainFX':
        return [
            'tether',
            'usd-coin',
            'binance-usd',
            'dai',
            #'usdp',
            'gemini-dollar',
            'tusd']


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
    coin_dict = {}
    for data_provider in TARGET_DATA_PROVIDERS:
        print(f"Fetching data from {data_provider}")
        coins = get_coin_data(data_provider)
        coin_dict[data_provider] = coins

    df = pd.DataFrame.from_dict(coin_dict)
    print(df)

     # export df to excel
    df.to_excel('stablecoins.xlsx')

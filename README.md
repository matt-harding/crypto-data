# Crypto Data Provider Comparison

The point of this work is to pull market data for the top 25 stable coins by market cap from five providers; CoinGecko, CoinMarkerCap, CoinMetrics, CryptoCompare & OnChainFX.
The outcome of this work is to assertain which provider is most appropriate.

The market data we are interested in is Price (USD), Market Cap, Circulating Supply, Total Supply & 24h volume

## OnChainFX

### Intro
OnChainFX pulls data from Messari so will be refering to their API
Without an API key, requests are rate limited to 20 requests per minute and 1000 requests per day. 
Users that create an account will have slightly higher limits of 30 requests per minute and 2000 requests per day. 
PRO users have the highest limit at 60 requests per minute up to a maximum of 4000 requests per day.

### Coverage


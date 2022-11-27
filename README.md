# Crypto Data Provider Comparison

The point of this work is to pull market data for the top 25 stable coins by market cap from five providers; CoinGecko, CoinMarkerCap, CoinMetrics, CryptoCompare & OnChainFX.
The outcome of this work is to assertain which provider is most appropriate.

The market data we are interested in is Price (USD), Market Cap, Circulating Supply, Total Supply & 24h volume

## OnChainFX

### **Intro**
* OnChainFX pulls data from Messari so will be refering to their API
* Without an API key, requests are rate limited to 20 requests per minute and 1000 requests per day. 
* Users that create an account will have slightly higher limits of 30 requests per minute and 2000 requests per day. 
* PRO users have the highest limit at 60 requests per minute up to a maximum of 4000 requests per day.

#### Pros
* First Party Python library
* Easy to use API
* Example Jupyter notebooks (https://github.com/messari/messari-python-api/blob/master/examples/notebooks)

#### Cons
* Small limit for usage without API key
* No total supply variable only liquid and circulating

### **Metrics**
https://messari.io/report/messari-proprietary-methods

#### market_data_price_usd
Since every cryptoasset can be traded on more than one exchange and as more than one pair (e.g., BTC/USD, BTC/USDT, BTC/EUR), we need a way to aggregate these different prices. The Messari aggregate price is a 24-hour volume-weighted average (VWAP) across various exchanges and pairs, quoted in USD.

#### marketcap_current_marketcap_usd

For a given asset, the "Reported Volume" metric refers to the aggregate volume across a list of most active exchanges.
It is well known that many exchanges conduct wash trading practices in order to inflate trading volume. They are incentivized to report inflated volumes in order to attract traders. "Real Volume” refers to the total volume on the exchanges that we believe with high level of confidence are free of wash trading activities. They tend to be regulated exchanges. They are a subset of the list of exchanges above. However, that does not necessarily mean that the volume reported by other exchanges is 100% wash trades. As such, the Real Volume underestimates the total global volume.


#### market_data_real_volume_last_24_hours
The circulating supply acknowledges that tokens may be held by projects/foundations which have no intent to sell down their positions, but which have not locked up supply in a formal contract. Thus, circulating supply does not include known project treasury holdings (which can be significant). Note that an investor must carefully consider both liquid and circulating supplies when evaluating an asset, and the two can vary significantly. A risk of depending entirely on circulating supply is that the number can change dramatically based on discretionary sales from project treasuries.


## CoinMetrics

#### **Intro**
* The community version of API has the limit of 1000 requests per 10 minutes sliding window for an IP address.
* The paid version of API has the limit of 6000 requests per 20 seconds sliding window for an API key.

#### Pros
* Extensive documentation
* Option for WebSocket streaming
* Metrics per exchange
* First party Python API client

#### Cons
* Limited coverage for desired metrics (possibly others avaiable with paid account)
* Complex API structure. Multiple calls required to build dataset
* No volume metric without API key

#### **Metrics**
Frequency 1d

#### PriceUSD (Removed in favour of ReferenceRateUSD)
The fixed closing price of the asset as of 00:00 UTC the following day (i.e., midnight UTC of the current day) denominated in USD. This price is generated by Coin Metrics' fixing/reference rate service. Real-time PriceUSD is the fixed closing price of the asset as of the timestamp set by the block's miner.

Available frequencies: 1b & 1d

#### ReferenceRateUSD
The price of an asset quoted in U.S. dollars using a framework to select high quality constituent markets and a methodology that is resistant manipulation.

Available frequencies: 1s, 1m ,1h, 1d, 1d-ny-close

#### CapMrktCurUSD
The sum USD value of the current supply. Also referred to as network value or market capitalization.

Available frequencies: 1d

Not supported : TerraUSD, Stasis Eur, Fei USD, Frax, Frax Share, Neutrino Dollar, DigitalBits, Pax Dollars

#### SplyActEver
The sum of unique native units held by accounts that transacted at least once up to that interval. Native units that transacted more than once are only counted once.

Available frequencies: 1d

## CoinGecko

* Free public api with no keys required

#### Pros

* Simple API

#### Cons

* Only third party python library
* Limited coin coverage
* Basic documentation

#### **Metrics**
https://www.coingecko.com/en/glossary

##### Circulating Supply
Circulating supply can be defined as the supply that is currently in the hands of the general public.In the case of fairly mined proof-of-work systems (eg. Bitcoin), the total supply is approximately equivalent to the circulating supply, as there are no token generation events which puts large amounts of tokens in the hands of a select few. On the contrary, initial coin offering (ICO) which have token generation events typically have a lower circulating supply vs. the total supply, such that: Circulating supply = Total Supply - Team tokens - Foundation tokens - Locked tokens




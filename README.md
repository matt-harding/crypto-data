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

Assets Supported for 1d frequency: ['1inch', 'aave', 'ada', 'ae', 'aion', 'alcx', 'algo', 'alpha', 'ant', 'ape', 'api3', 'atom', 'audio', 'avax', 'avaxx', 'badger', 'bal', 'bat', 'bch', 'bnb', 'bnb_bc', 'bnb_eth', 'bnt', 'bsv', 'btc', 'btg', 'btm', 'busd', 'cel', 'cennz', 'comp', 'cro', 'crv', 'ctxc', 'cvc', 'cvx', 'dai', 'dash', 'dcr', 'dgb', 'dgx', 'doge', 'dot', 'drgn', 'elf', 'eng', 'enj', 'ens', 'eos', 'eos_eth', 'etc', 'eth', 'ethos', 'fei_eth', 'fil', 'ftt', 'fun', 'fxc', 'gala', 'gas', 'glm', 'gno', 'gnt', 'grin', 'grt', 'gusd', 'hbtc', 'hedg', 'ht', 'husd', 'icp', 'icx', 'kcs', 'kin3', 'knc', 'ldo', 'lend', 'leo_eos', 'leo_eth', 'link', 'looks', 'loom', 'lpt', 'lrc', 'lsk', 'ltc', 'luna', 'lusd', 'maid', 'mana', 'matic_eth', 'mco', 'mkr', 'mpl', 'mtl_metal', 'nas', 'neo', 'nexo', 'nftx', 'nmr', 'nxm', 'ogn', 'okb', 'omg', 'pax', 'paxg', 'pay', 'perp', 'pivx', 'poly', 'powr', 'ppt', 'qash', 'qnt', 'qtum', 'rad', 'rai_eth', 'ren', 'renbtc', 'rep', 'rev_eth', 'rook', 'rsr', 'sai', 'sand', 'shib', 'skl', 'snt', 'snx', 'sol', 'spell', 'srm', 'srn', 'stmx', 'storj', 'sushi', 'swrv', 'toke', 'trx', 'trx_eth', 'tusd', 'uma', 'uni', 'uqc', 'usdc', 'usdk', 'usdt', 'usdt_eth', 'usdt_omni', 'usdt_trx', 'ust', 'vet', 'vtc', 'waves', 'wbtc', 'weth', 'wnxm', 'wtc', 'xaut', 'xem', 'xlm', 'xmr', 'xrp', 'xtz', 'xvg', 'yfi', 'zec', 'zil', 'zrx']

#### ReferenceRateUSD
The price of an asset quoted in U.S. dollars using a framework to select high quality constituent markets and a methodology that is resistant manipulation.

Available frequencies: 1s, 1m ,1h, 1d, 1d-ny-close

Assets Supported for 1d frequency: ['1inch', 'aave', 'abbc', 'abt', 'aca', 'ach', 'ada', 'adx', 'ae', 'aergo', 'agi', 'agld', 'aion', 'aioz', 'akro', 'akt', 'alcx', 'aleph', 'algo', 'alice', 'alpaca', 'alpha', 'alpine', 'amb', 'amp', 'ampl', 'anc', 'angle', 'ankr', 'ant', 'aoa', 'ape', 'api3', 'appc', 'ar', 'ardr', 'ark', 'arpa', 'arv', 'asd', 'asm', 'ast', 'astr', 'astro', 'ata', 'atlas', 'atom', 'auction', 'aud', 'audio', 'auto', 'ava', 'avax', 'avt', 'axs', 'badger', 'bake', 'bal', 'band', 'bat', 'bcd', 'bch', 'bcn', 'beam', 'bel', 'berry', 'beta', 'bfc', 'bft', 'bico', 'bidr', 'bit', 'bix', 'blz', 'bnb', 'bnt', 'bnx', 'boa', 'boba', 'bond', 'bora', 'boson', 'brl', 'bsv', 'btc', 'btcst', 'btg', 'btm', 'btmx', 'btrst', 'bts', 'btt', 'bttc', 'busd', 'bzrx', 'c98', 'cad', 'cake', 'cdt', 'ceek', 'cel', 'celo', 'celr', 'cennz', 'cfx', 'chat', 'chess', 'chf', 'chr', 'chsb', 'chz', 'city', 'ckb', 'clv', 'cmt', 'cnd', 'cnn', 'comp', 'conv', 'coti', 'coval', 'cpay', 'cqt', 'cream', 'cro', 'crpt', 'crv', 'csp', 'cspr', 'ctc', 'ctk', 'ctsi', 'ctxc', 'cube', 'cudos', 'cvc', 'cvp', 'cvt', 'cvx', 'dag', 'dai', 'dao', 'dar', 'dash', 'data', 'dbc', 'dcr', 'ddx', 'dent', 'dfi', 'dgb', 'dgd', 'dgtx', 'dgx', 'dia', 'dmg', 'dnt', 'dock', 'dodo', 'doge', 'dora', 'dot', 'drep', 'drgn', 'dta', 'dusk', 'dvi', 'dx', 'dydx', 'eden', 'efi', 'egld', 'ela', 'elf', 'elon', 'eng', 'enj', 'ens', 'eos', 'erg', 'ern', 'etc', 'eth', 'ethos', 'ethw', 'etn', 'etp', 'eul', 'eur', 'euroc', 'eurs', 'eurt', 'evx', 'ewt', 'farm', 'fct', 'fei', 'fet', 'fida', 'fil', 'fire', 'fis', 'fitfi', 'flm', 'floki', 'flow', 'flux', 'foam', 'for', 'forth', 'fox', 'frax', 'front', 'ftm', 'ftt', 'fun', 'fx', 'fxs', 'gal', 'gala', 'gari', 'gas', 'gbp', 'gbpt', 'gfi', 'ghst', 'glm', 'glmr', 'gm', 'gmt', 'gno', 'go', 'gods', 'grin', 'grs', 'grt', 'gst', 'gt', 'gtc', 'gtc_gamecom', 'gusd', 'gxs', 'gyen', 'hbar', 'hc_hypercash', 'hedg', 'hegic', 'high', 'hive', 'hkd', 'hns', 'hnt', 'hot_holo', 'hpt', 'ht', 'husd', 'hxro', 'icp', 'icx', 'idex', 'idrt', 'ignis', 'iht', 'ilv', 'imx', 'inj', 'inv', 'iost', 'iotx', 'iris', 'itc', 'jasmy', 'joe', 'jpy', 'jst', 'juv', 'kai', 'kan', 'kava', 'kcs', 'kda', 'keep', 'key', 'kin', 'klay', 'klv', 'kmd', 'knc', 'kok', 'kp3r', 'krl', 'krw', 'ksm', 'lamb', 'lba', 'lbc', 'lcx', 'ldo', 'leo', 'lina', 'link', 'lit', 'loka', 'lon', 'looks', 'loom', 'lpt', 'lqty', 'lrc', 'lsk', 'ltc', 'lto', 'lun', 'luna', 'luna2', 'lusd', 'lym', 'maid', 'mana', 'maps', 'mask', 'math', 'matic', 'mbl', 'mbox', 'mc', 'mco', 'mco2', 'mda', 'mdt', 'mdx', 'med', 'media', 'meta', 'metis', 'mft', 'mim', 'mina', 'miota', 'mir', 'mith', 'mkr', 'mln', 'mob', 'mof', 'mona', 'movr', 'mpl', 'msol', 'mta', 'mtl_metal', 'musd', 'mx', 'mxc', 'nano', 'nas', 'nav', 'ncash', 'nct', 'near', 'neo', 'nest', 'nexo', 'nft', 'nftx', 'ngn', 'nii', 'nim', 'nkn', 'nmr', 'noia', 'nrg', 'nu', 'nuls', 'nxt', 'nym', 'oax', 'ocean', 'ocn', 'octo', 'ogn', 'ohm', 'okb', 'om', 'omg', 'one_harmony', 'ong_ontologygas', 'ont', 'ooki', 'op', 'orbs', 'orca', 'orn', 'osmo', 'ost', 'oxt', 'oxy', 'pai', 'pax', 'paxg', 'pay', 'people', 'perp', 'pha', 'phx', 'pivx', 'pla', 'plu', 'pnk', 'pnt', 'poa', 'polis', 'pols', 'poly', 'pond', 'powr', 'ppt', 'pro', 'prom', 'prq', 'psg', 'psp', 'pstake', 'pundix', 'pyr', 'qash', 'qi', 'qkc', 'qnt', 'qrdo', 'qsp', 'qtum', 'quick', 'raca', 'rad', 'rai', 'ramp', 'rare', 'rari', 'ray', 'rbn', 'rcn_ripiocreditnetwork', 'rdd', 'rdn', 'reef', 'ren', 'renbtc', 'rep', 'req', 'rev', 'revv', 'rgt', 'rif', 'rlc', 'rly', 'rndr', 'rook', 'rose', 'rsr', 'rub', 'rune', 'rvn', 'samo', 'sand', 'santos', 'sbr', 'sc', 'scrt', 'sdn', 'seele', 'senso', 'sfi', 'sfp', 'sgb', 'sgd', 'shib', 'shping', 'shr', 'skl', 'slp', 'sngls', 'snt', 'snx', 'sol', 'solve', 'sos', 'spell', 'srm', 'srn', 'ssx', 'starl', 'steem', 'step', 'steth', 'stg', 'stmx', 'storj', 'stpt', 'strax', 'strk', 'strp', 'stx', 'suku', 'sun', 'super', 'susd', 'sushi', 'swap', 'sweat', 'swftc', 'swrv', 'sxp', 'syn', 'sys', 't', 'tel', 'tfuel', 'theta', 'tlm', 'tnb', 'toke', 'tomo', 'ton', 'torn', 'trac', 'trb', 'tribe', 'tru', 'trx', 'try', 'tryb', 'tt', 'tulip', 'tusd', 'tvk', 'twt', 'uah', 'ubt', 'uma', 'unfi', 'uni', 'uos', 'uqc', 'usdc', 'usdd', 'usdk', 'usdn', 'usdp', 'usdt', 'ust', 'utk', 'velo', 'vet', 'vgx', 'via', 'vib', 'vlx', 'voxel', 'vra', 'vsys', 'vtc', 'vtho', 'wan', 'waves', 'waxp', 'wbtc', 'wcfg', 'wemix', 'wicc', 'win_wink', 'wluna', 'wncg', 'wnxm', 'woo', 'wpr', 'wrx', 'wtc', 'wxt', 'xaut', 'xch', 'xcn', 'xdb', 'xdc', 'xec', 'xem', 'xhv', 'xlm', 'xmr', 'xprt', 'xrp', 'xtz', 'xvg', 'xvs', 'xym', 'xyo', 'yfi', 'yfii', 'ygg', 'yoyow', 'zb', 'zbc', 'zec', 'zen', 'zil', 'zks', 'zrx']

#### CapMrktCurUSD
The sum USD value of the current supply. Also referred to as network value or market capitalization.

Available frequencies: 1d

Not supported : TerraUSD, Stasis Eur, Fei USD, Frax, Frax Share, Neutrino Dollar, DigitalBits, Pax Dollars

Assets supported for 1d frequency: ['1inch', 'aave', 'ada', 'ae', 'aion', 'algo', 'alpha', 'ant', 'ape', 'api3', 'atom', 'audio', 'avax', 'badger', 'bal', 'bat', 'bch', 'bnb', 'bnb_bc', 'bnb_eth', 'bnt', 'bsv', 'btc', 'btg', 'btm', 'busd', 'cel', 'cennz', 'comp', 'cro', 'crv', 'ctxc', 'cvc', 'cvx', 'dai', 'dash', 'dcr', 'dgb', 'dgx', 'doge', 'dot', 'drgn', 'elf', 'eng', 'ens', 'eos', 'eos_eth', 'etc', 'eth', 'ethos', 'fil', 'ftt', 'fun', 'fxc', 'gala', 'gas', 'glm', 'gno', 'gnt', 'grin', 'grt', 'gusd', 'hbtc', 'hedg', 'ht', 'husd', 'icp', 'icx', 'kcs', 'kin3', 'knc', 'ldo', 'lend', 'leo_eos', 'leo_eth', 'link', 'loom', 'lpt', 'lrc', 'lsk', 'ltc', 'luna', 'lusd', 'maid', 'mana', 'matic_eth', 'mco', 'mkr', 'mpl', 'mtl_metal', 'nas', 'neo', 'nexo', 'nmr', 'nxm', 'ogn', 'okb', 'omg', 'pax', 'paxg', 'pay', 'perp', 'pivx', 'poly', 'powr', 'ppt', 'qash', 'qnt', 'qtum', 'rad', 'rai_eth', 'ren', 'renbtc', 'rep', 'rev_eth', 'rsr', 'sai', 'shib', 'skl', 'snt', 'snx', 'sol', 'spell', 'srm', 'srn', 'stmx', 'storj', 'sushi', 'swrv', 'trx', 'trx_eth', 'tusd', 'uma', 'uni', 'usdc', 'usdk', 'usdt', 'usdt_eth', 'usdt_omni', 'usdt_trx', 'ust', 'vtc', 'waves', 'wbtc', 'weth', 'wnxm', 'wtc', 'xaut', 'xem', 'xlm', 'xmr', 'xrp', 'xtz', 'xvg', 'yfi', 'zec', 'zil', 'zrx']

#### SplyActEver
The sum of unique native units held by accounts that transacted at least once up to that interval. Native units that transacted more than once are only counted once.

Available frequencies: 1d

Assets supported for 1d frequency: ['1inch', 'aave', 'ada', 'ae', 'aion', 'algo', 'alpha', 'ant', 'bal', 'bat', 'bch', 'bnb', 'bnb_eth', 'bsv', 'btc', 'btg', 'btm', 'busd', 'cennz', 'comp', 'cro', 'crv', 'ctxc', 'cvc', 'dai', 'dash', 'dcr', 'dgb', 'dgx', 'doge', 'dot', 'drgn', 'elf', 'eng', 'eos_eth', 'etc', 'eth', 'ethos', 'ftt', 'fun', 'fxc', 'fxc_eth', 'gas', 'gno', 'gnt', 'gusd', 'hbtc', 'hedg', 'ht', 'husd', 'icn', 'icp', 'icx', 'kcs', 'kin1', 'knc', 'lend', 'leo_eth', 'link', 'loom', 'lpt', 'lrc', 'lsk', 'ltc', 'maid', 'mana', 'matic_eth', 'mco', 'mkr', 'mtl_metal', 'nas', 'neo', 'nxm', 'omg', 'pax', 'paxg', 'pay', 'perp', 'pivx', 'poly', 'powr', 'ppt', 'qash', 'qnt', 'qtum', 'ren', 'renbtc', 'rep', 'rev_eth', 'rhoc', 'sai', 'salt', 'snt', 'snx', 'srm', 'srn', 'sushi', 'swrv', 'trx_eth', 'tusd', 'uma', 'uni', 'usdc', 'usdk', 'usdt', 'usdt_eth', 'usdt_omni', 'usdt_trx', 'veri', 'vet', 'vtc', 'wbtc', 'weth', 'wnxm', 'wtc', 'xaut', 'xlm', 'xrp', 'xtz', 'xvg', 'yfi', 'zec', 'zil', 'zrx']


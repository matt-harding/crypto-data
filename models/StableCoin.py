from dataclasses import dataclass

@dataclass
class StableCoin:
    """Class for condensing exchange data to just the props we care about"""
    id: str = ''
    data_provider: str = ''
    symbol: str = ''
    name: str = ''
    market_cap: float = 0
    circulating_supply: float = 0
    total_supply: float = 0
    twentyfourhour_volume: float = 0
    price: float = 0
    last_updated: str = ''
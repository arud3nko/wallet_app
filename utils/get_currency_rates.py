from __future__ import annotations
import aiohttp
import asyncio
from dataclasses import dataclass
from typing import List


@dataclass
class Currency:
    code: str
    rate: float = 0.0


API_KEY = "cur_live_JIIL90ZMCvp9Kexfr9m3tTLv1zuiiJTZk20VKW8C"
BASE_URL = "https://api.currencyapi.com/v3/latest"


async def fetch_currency_rate(session: aiohttp.ClientSession, currency_code: str) -> float:
    params = {
        "apikey": API_KEY,
        "base_currency": "USDT"
    }
    async with session.get(BASE_URL, params=params) as response:
        if response.status == 200:
            data = await response.json()
            rate = data["data"].get(currency_code, {}).get("value", 0.0)
            return rate
        else:
            raise Exception(f"Failed to fetch rate for {currency_code}. Status: {response.status}")


async def update_currency_rates(currencies: List[Currency]) -> List[Currency]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_currency_rate(session, currency.code) for currency in currencies]
        rates = await asyncio.gather(*tasks)
        for currency, rate in zip(currencies, rates):
            currency.rate = rate
    return currencies


async def main():
    # Пример списка валют
    currencies = [
        Currency(code="EUR"),
        Currency(code="USD"),
        Currency(code="CAD"),
        Currency(code="BTC"),  # Bitcoin
        Currency(code="ETH"),  # Ethereum
    ]

    updated_currencies = await update_currency_rates(currencies)
    for currency in updated_currencies:
        print(f"Currency: {currency.code}, Rate in USDT: {currency.rate}")

# Запуск основного цикла событий
if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import time

import httpx

URLS = [
    "https://open.er-api.com/v6/latest/USD",
    "https://open.er-api.com/v6/latest/SAR",
    "https://open.er-api.com/v6/latest/AED",
]


def one_by_one() -> None:
    for url in URLS:
        rate = httpx.get(url, timeout=10).json()["rates"]["PKR"]
        print(f"{url[-3:]}: Rs {rate:.2f}")


async def get_rate(client: httpx.AsyncClient, url: str) -> float:
    response = await client.get(url, timeout=10)
    return response.json()["rates"]["PKR"]


async def all_together() -> None:
    async with httpx.AsyncClient() as client:
        rates = await asyncio.gather(*(get_rate(client, url) for url in URLS))
    for url, rate in zip(URLS, rates):
        print(f"{url[-3:]}: Rs {rate:.2f}")


start = time.perf_counter()
one_by_one()
print(f"Ek ek karke: {time.perf_counter() - start:.2f} sec")

start = time.perf_counter()
asyncio.run(all_together())
print(f"Ek saath: {time.perf_counter() - start:.2f} sec")

import asyncio
import aiohttp
import time

async def fetchfromGoogle():
    url = 'https://www.google.com'
    session = aiohttp.ClientSession()
    resp = await session.get(url)
    await resp.content.read()
    await session.close()

async def main():
    print(time.strftime('%X'))
    await asyncio.gather(
        *[
            fetchfromGoogle() for  _ in range(200)
        ]
    )
    print(time.strftime('%X'))

if __name__ == '__main__':
    asyncio.run(main())
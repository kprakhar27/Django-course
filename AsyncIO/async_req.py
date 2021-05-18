import asyncio
import aiohttp
import time

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

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
            fetchfromGoogle() for  _ in range(20)
        ]
    )
    print(time.strftime('%X'))

if __name__ == '__main__':
    asyncio.run(main())
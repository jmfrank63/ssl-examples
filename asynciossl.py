# -*- coding: utf-8 -*-
import asyncio
import aiohttp
import ssl
import os

async def amain():
    os.environ['SSLKEYLOGFILE'] = 'keylog.txt'
    context = ssl.create_default_context()
    conn = aiohttp.TCPConnector(ssl=context)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get('https://httpbin.org/xml') as resp:
            headers = resp.headers
            result = await resp.text()
            print(headers)
            print(result)            

asyncio.run(amain())

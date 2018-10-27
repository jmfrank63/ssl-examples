import asks
import trio
import os

asks.init(trio)

path_list = ['https://httpbin.org/xml','https://postman-echo.com']

results = []


async def grabber(s, path):
    r = await s.get(path)
    results.append(r)
    print(r.text)


async def main(path_list):
    os.environ['SSLKEYLOGFILE'] = 'keylog.txt'
    from asks.sessions import Session
    s = Session('https://httpbin.org', connections=2)
    async with trio.open_nursery() as n:
        await trio.sleep(0)
        for path in path_list:
            n.start_soon(grabber, s, path)

trio.run(main, path_list)
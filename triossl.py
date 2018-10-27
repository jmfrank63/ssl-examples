# -*- coding: utf-8 -*-

import trio
import os

hostname = 'httpbin.org'
port = 443

async def child1(ssl_stream):
    print("  child1: started! sending now...")
    await ssl_stream.do_handshake()
    await ssl_stream.send_all(b"GET /xml HTTP/1.1\r\nHost: " + bytes(hostname, 'utf-8') + b"\r\n\r\n")
    print("  child1: Done sending!")

async def child2(ssl_stream):
    print("  child2: started! receiving now...")
    result = await ssl_stream.receive_some(100000)
    print(result.decode('ascii'))
    print("  child2: Done receiving!")

async def parent():
    print("parent: starting request!")
    os.environ['SSLKEYLOGFILE'] = 'keylog.txt'
    #context = trio.ssl.create_default_context()
    ssl_stream = await trio.open_ssl_over_tcp_stream(hostname, port)

    async with trio.open_nursery() as nursery:
        print("parent: spawning sender...")
        nursery.start_soon(child1, ssl_stream)

        print("parent: spawning receiver...")
        nursery.start_soon(child2, ssl_stream)

        print("parent: waiting for sender and receiver to finish...")
        # -- we exit the nursery block here --
    print("parent: Request done!")

trio.run(parent)

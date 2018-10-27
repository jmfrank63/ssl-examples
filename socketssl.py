import socket
import ssl
import os

hostname = 'httpbin.org'
port = 443

os.environ['SSLKEYLOGFILE'] = 'keylog.txt'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        ssock.send(b"GET /xml HTTP/1.1\r\nHost: " + bytes(hostname, 'utf-8') + b"\r\n\r\n")
        print(ssock.version())
        resp = ssock.recv(10000)
        print(resp.decode('ascii'))

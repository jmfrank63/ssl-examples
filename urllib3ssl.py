import certifi
import urllib3
import ssl
import os

os.environ['SSLKEYLOGFILE'] = 'keylog.txt'
context = ssl.create_default_context()

https = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where(),
    ssl_context=context)

resp = https.request('GET','https://httpbin.org/xml')
print(resp.data.decode('ascii'))

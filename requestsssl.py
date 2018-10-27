import requests
import ssl
import os

os.environ['SSLKEYLOGFILE'] = 'keylog.txt'
context = ssl.create_default_context()
resp = requests.get('https://httpbin.org/xml')

print(resp.text)

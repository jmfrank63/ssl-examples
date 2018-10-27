import os
from ssl import create_default_context

from requests import Session
from requests.adapters import HTTPAdapter


class MyHTTPAdapter(HTTPAdapter):
    def set_ssl_context(self, ssl_context):
        self.init_poolmanager(self._pool_connections, self._pool_maxsize,
                              block=self._pool_block, ssl_context=ssl_context)


os.environ.setdefault('SSLKEYLOGFILE', 'keylog.txt')

session = Session()
adapter = MyHTTPAdapter()
adapter.set_ssl_context(create_default_context())
session.mount('https://', adapter)

session.get('https://httpbin.org/xml')

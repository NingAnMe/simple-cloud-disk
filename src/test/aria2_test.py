import unittest

from ..aria2 import Aria2
from ..config import *


class TestAria2(unittest.TestCase):

    def test_init(self):
        a = Aria2()
        self.assertEqual(a.jsonrpc_version, '2.0')
        self.assertEqual(a.jsonrpc_url, 'http://localhost:6800/jsonrpc')
        self.assertEqual(a.request, {'jsonrpc': '2.0', 'id': 'scp'})
        self.assertTrue(a.secret is None)
        a = Aria2(secret=SECRET)
        self.assertEqual(a.secret, SECRET)

    def test_download_uri(self):
        a = Aria2(secret=SECRET)
        uri = 'https://files.pythonhosted.org/packages/45/ae/8a0ad77defb7cc903f09e551d8' \
              '8b443304a9bd6e6f124e75c0fbbf6de8f7/pip-18.1.tar.gz'
        response = a.download_file(uri, 'uri')
        self.assertTrue('result' in response)

        uri = 'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'
        response = a.download_file(uri, 'uri')
        self.assertTrue('result' in response)


if __name__ == '__main__':
    unittest.main()

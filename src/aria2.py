import base64
import json
import requests


class Aria2:

    def __init__(self, jsonrpc_url='http://localhost:6800/jsonrpc', secret=None):
        """
        :param jsonrpc_url: 'http://localhost:6800/jsonrpc'
        :param secret:
        """
        self.jsonrpc_version = '2.0'  # jsonrpc 版本
        self.request = {'jsonrpc': self.jsonrpc_version,
                        'id': 'scd'}
        self.jsonrpc_url = jsonrpc_url
        self.secret = secret

    def download_file(self, uri, method):
        """
        如果 method == 'uri'： HTTP/FTP/SFTP/BitTorrent URIs
        http://example.org/mylinux.iso
        https://example.org/mylinux.iso
        ftp://example.org/mylinux.iso
        sftp://example.org/mylinux.iso
        'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'

        如果 method == 'torrent': Torrent file
        http://example.org/mylinux.torrent

        如果 method == 'metalink': Metalink
        http://example.org/mylinux.metalink

        参考： https://aria2.github.io/manual/en/html/aria2c.html#rpc-interface

        :param uri: HTTP/FTP/SFTP/BitTorrent URIs  or Torrent file or Metalink
        :param method: 'uri' or 'torrent' or 'metalink'
        :return:
        """
        if method == 'uri':
            m = 'aria2.addUri'
            f = uri
        elif method == 'torrent':
            m = 'aria2.addTorrent'
            f = base64.b64encode(open(uri).read())
        elif method == 'metalink':
            m = 'aria2.addMetalink'
            f = base64.b64encode(open(uri).read())
        else:
            raise(KeyError, 'Method error: {0}'.format(method))

        params = list()
        if self.secret is not None:
            params.append('token:{0}'.format(self.secret))
        params.append([f])

        self.request['method'] = m
        self.request['params'] = params

        json_request = json.dumps(self.request)
        response = requests.post(self.jsonrpc_url, json_request)
        return response.json()

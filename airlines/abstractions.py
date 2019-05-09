import aiohttp
import logging


log = logging.getLogger(__name__)


class FareFinder:

    def __init__(self, url: str, username: str, password: str, headers: dict,
                 certificate: any, proxy: str or None, timeout: int,
                 verify_ssl: bool):
        self.url = url
        self.headers = headers
        self.username = username
        self.password = password
        self.certificate = certificate
        self.proxy = proxy
        self.timeout = timeout
        self.verify_ssl = verify_ssl

    async def get(self, data, **kwargs):
        # log.debug('----- get')
        # log.debug(f'{data}')
        # log.debug(f'{kwargs}')
        return await self._request('get', data=data, **kwargs)

    async def post(self, data, **kwargs):
        return await self._request('post', data, **kwargs)

    async def _request(self, method, data, auth=None, **kwargs):

        # log.debug('----- _request')
        # log.debug(f'{method}')
        # log.debug(f'{data}')
        # log.debug(f'{kwargs}')

        if self.username and self.password:
            auth = aiohttp.BasicAuth(login=self.username,
                                     password=self.password)
        _kwargs = {
            'method': method,
            'url': kwargs.get('url') or self.url,
            'headers': kwargs.get('headers') or self.headers,
            'timeout': self.timeout,
            'proxy': kwargs.get('proxy') or self.proxy
        }

        if method == 'post':
            _kwargs.update({'json': data})
        elif method == 'get':
            _kwargs.update({'params': data})

        try:
            connector = aiohttp.TCPConnector(verify_ssl=self.verify_ssl)
            async with aiohttp.ClientSession(
                    auth=auth, connector=connector) as session:
                async with session.request(**_kwargs) as response:
                    return await self.response_handling(response)
        except Exception as e:
            log.error(f'TCPConnector error: {e}')
            return None

    async def response_handling(self, data):
        raise NotImplementedError()

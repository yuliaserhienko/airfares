import logging

from airlines.abstractions import FareFinder
from airlines.ryanair.settings import RYANAIR_API_URL
from airlines.ryanair.constants import ConstantsRyanair


log = logging.getLogger(__name__)


class RyanairFareFinder(FareFinder):

    _kwargs = {
        'url': RYANAIR_API_URL,
        'headers': None,
        'username': '',
        'password': '',
        'certificate': None,
        'proxy': None,
        'timeout': 30,
        'verify_ssl': True
    }

    def get_request_url(self, direction=ConstantsRyanair.one_way.name):
        request_url = f'{self.url}{getattr(ConstantsRyanair, direction).value}'
        log.debug(f'request_url >>> {request_url}')
        return request_url

    def __init__(self,
                 url=RYANAIR_API_URL,
                 username='',
                 password='',
                 headers=None,
                 certificate=None,
                 proxy=None,
                 timeout=None,
                 verify_ssl=True):
        super().__init__(url=url,
                         username=username,
                         password=password,
                         headers=headers,
                         certificate=certificate,
                         proxy=proxy,
                         timeout=timeout,
                         verify_ssl=verify_ssl)

    async def best_prices(self):

        headers = {'Accept': 'application/json, text/plain, */*',
                   'DNT': '1',
                   'Origin': 'https://www.ryanair.com',
                   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/74.0.3729.131 Safari/537.36'}

        data_ow = {'departureAirportIataCode': 'KBP',
                   'language': 'en',
                   'limit': '32',
                   'market': 'en-gb',
                   'offset': '0',
                   'outboundDepartureDateFrom': '2019-05-03',
                   'outboundDepartureDateTo': '2020-03-28',
                   'priceValueTo': '150'}

        data_rt = {'departureAirportIataCode': 'KBP',
                   'durationFrom': '01',
                   'durationTo': '03',
                   'inboundDepartureDateFrom': '2019-05-03',
                   'inboundDepartureDateTo': '2020-03-28',
                   'language': 'en',
                   'limit': '16',
                   'market': 'en-gb',
                   'offset': '0',
                   'outboundDepartureDateFrom': '2019-05-03',
                   'outboundDepartureDateTo': '2020-03-28',
                   'priceValueTo': '150'}

        response = await self.get(data_ow,
                                  url=self.get_request_url(),
                                  headers=headers)
        # log.debug(f' best_prices --> status: {getattr(response, "status", None)}')
        # log.debug(f'--> text: {getattr(response, "text", None)}')
        # response = await self.response_handling(response)
        return response

    async def response_handling(self, data):
        log.debug(f'response_handling > data >> {data}')
        # response = await data
        # log.debug(f'response_handling > response >> {response}')
        # log.debug(f'status: {getattr(data, "status", None)}')
        # log.debug(f'text: {getattr(data, "text", None)}')
        return await data.json()


ryanair_fare_finder = RyanairFareFinder()

from aiohttp import web

from airlines.ryanair.requester import ryanair_fare_finder


async def weekends(request):
    # response = ryanair_fare_finder.best_prices()
    response = {'data': []}
    return web.json_response(response)


async def best_prices(request):
    response = await ryanair_fare_finder.best_prices()
    return web.json_response(response)

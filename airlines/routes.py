from aiohttp import web
from airlines.ryanair import handlers as ryanair_handlers

airline_routes = [
    web.get('/ryanair/weekends/', ryanair_handlers.weekends),
    web.get('/ryanair/best-prices/', ryanair_handlers.best_prices)
]

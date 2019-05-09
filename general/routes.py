from aiohttp import web

from airlines.routes import airline_routes
from general.handlers import service_status


routes = [
    web.get('/', service_status)
] + airline_routes


async def setup_routes(app):
    app.add_routes(routes)

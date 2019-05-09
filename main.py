import os
import logging
import datetime

import asyncio
from aiohttp import web

from general.routes import setup_routes


async def init_web_app():
    try:
        _app = web.Application(debug=True, middlewares=[])
        _app['start_time'] = datetime.datetime.now()
        await setup_routes(_app)
        # setup_cache(app_, cache_type='redis', backend_config=redis_config)
        # setup_cache(app_)
        return _app
    except Exception as e:
        print(e)

logging.getLogger('asyncio')
logging.basicConfig(
    filename=os.environ.get('LOG_FILE'),
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_web_app())

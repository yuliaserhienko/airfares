import os

bind = f"{os.environ.get('HOST')}:{os.environ.get('PORT')}"
timeout = int(os.environ.get('TIMEOUT'))
workers = int(os.environ.get('WORKERS'))
worker_class = "aiohttp.worker.GunicornWebWorker"
reload = True

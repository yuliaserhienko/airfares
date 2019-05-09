from aiohttp import web


async def service_status(request):
    # name = request.match_info.get('name', "Anonymous")
    # text = "Hello, " + name
    return web.json_response({'status': 1})

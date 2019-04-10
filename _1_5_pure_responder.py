# -*- coding: utf-8 -*-
import responder

api = responder.API()

@api.route("/")
async def hello_world(req, resp):
    resp.text = "Hello World!"


if __name__ == '__main__':
    api.run(
        address='127.0.0.1',
        port=9999,
        debug=True,
        workers=1
    )

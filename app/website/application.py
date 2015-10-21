import tornado.web
import project_settings
from website.controllers import index


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler)
        ]

        settings = {
            "template_path": project_settings.TEMPLATE_PATH,
            "static_path": project_settings.STATIC_PATH,
            "debug": True,
        }

        tornado.web.Application.__init__(self, handlers, **settings)

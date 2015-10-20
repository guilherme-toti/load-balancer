import Settings
import tornado.ioloop
import tornado.web
import tornado.httpserver


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler)
        ]

        settings = {
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,
        }

        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


def main():
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9000)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

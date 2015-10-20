import tornado.ioloop
import tornado.httpserver
from website.application import Application


def main():
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9000)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

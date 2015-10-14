import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("from server 1")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == '__main__':
    application.listen(9000)
    tornado.ioloop.IOLoop.current().start()

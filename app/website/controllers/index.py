import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        name = self.get_body_argument('name', '')
        self.render("index.html", name=name)

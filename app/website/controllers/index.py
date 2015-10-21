import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/index.html")

    def post(self):
        username = self.get_body_argument('username', '')
        self.render("pages/index.html", username=username)

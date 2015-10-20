import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        nome = self.get_body_argument('nome', '')
        self.render("index.html", nome=nome)

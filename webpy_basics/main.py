import web

urls = (
    '/(.*)', 'Index'
)

app = web.application(urls, globals())


class Index:
    def GET(self, name):
        if not name:
            name = "World"
        return "Hello " + name.capitalize() + ". Hope you are doing well!"


if __name__ == "__main__":
    app.run()

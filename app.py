import web
from web import utils
web.config.debug = False

urls = (
    '/', "index",
    "/login", "login"
    )

app = web.application(urls, globals())
user = utils.Storage({ "name" : "", "auth" : False})
session = web.session.Session(app, web.session.DiskStore("session"), initializer = {
        "user" : user
    })
web.config._session = session  
render = web.template.render("templates")

class index:
    def GET(self):
        print session.user
        if not session.user.auth:
            raise web.seeother("/login")
        else:
            return "login "

class login:
    def GET(self):
        return render.login()
    def POST(self):
        user =  web.input()
        if user.get("name") == "admin" and user.get("password") == "admin":
            session.user.name = user.name
            session.user.auth = True
            raise web.seeother("/")
        else:
            raise web.seeother("/login")

if __name__ == "__main__":
    app.run()
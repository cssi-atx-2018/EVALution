import webapp2
from google.appengine.api import users
import jinja2
from google.appengine.ext import ndb

load = jinja2.FileSystemLoader(searchpath = './')
env = jinja2.Environment(loader = load)

class input(webapp2.RequestHandler):

    def get(self):

        template =  env.get_template("templates/loginu.html")
        template.render()
        user = users.User(self.request.get('email'))
        print ('user')
        if user:
            nickname = user.nickname()
            logout = users.create_logout_url()

        else:
            login = users.create_login_url('/')



app = webapp2.WSGIApplication([
('/login', input)

])

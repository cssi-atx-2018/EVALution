import webapp2
from google.appengine.api import users
import jinja2
from google.appengine.ext import ndb

load = jinja2.FileSystemLoader(searchpath = './')
env = jinja2.Environment(loader = load)

class input(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            self.response.write("You can Continue")
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
            nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            self.response.write('You must login')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
        self.response.write('<html><body>{}</body></html>'.format(greeting))
        

demo = webapp2.WSGIApplication([
('/login', input),

])

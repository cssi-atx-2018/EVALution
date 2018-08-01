'''This python code creates the main page of our glass bottle website, loads in
the main page template, the glass bottle template'''

import webapp2
import os
import jinja2

from google.appengine.api import users
from models import Post

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

user = users.get_current_user()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("templates/mainpage.html")
        self.response.write(start_template.render())

class LGBottleHandler(webapp2.RequestHandler):
    def get(self):
        bottle_template = jinja_env.get_template("templates/glassbottlelg.html")
        self.response.write(bottle_template.render())

    def post(self):
        text = self.request.get("entry")
        post = Post(post_content=text, post_user_id="")
        post.put()

class BottleHandler(webapp2.RequestHandler):
    def get(self):
        bottle_template = jinja_env.get_template("templates/glassbottle.html")
        self.response.write(bottle_template.render())
# need to fix so that it works only if you are logged in
    def post(self):
        post_template = jinja_env.get_template("templates/posts.html")
        text = self.request.get("entry")
        post = Post(post_content=text, post_user_id="")
        post.put()
        self.response.write(post_template.render())

class PostHandler(webapp2.RequestHandler):
    def get(self):
        post_template = jinja_env.get_template("templates/posts.html")
        self.response.write(post_template.render())

class LoginHandler(webapp2.RequestHandler):
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

class ResourceHandler(webapp2.RequestHandler):
    def get(self):
        resources_template = jinja_env.get_template("templates/resources.html")

class MusicHandler(webapp2.RequestHandler):
    def get(self):
        music_template = jinja_env.get_template("templates/music.html")

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_env.get_template("templates/about.html")
        self.response.write(about_template.render())

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/glass-bottle-lg", LGBottleHandler),
    ("/glass-bottle", BottleHandler),
    ("/posts", PostHandler),
    ("/login", LoginHandler),
    ("/resources", ResourceHandler),
    ("/music", MusicHandler),
    ("/about", AboutHandler)

], debug=True)

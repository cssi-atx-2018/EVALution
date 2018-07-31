'''This python code creates the main page of our glass bottle website, loads in
the main page template, the glass bottle template'''

import webapp2
import os
import jinja2


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("mainpage.html")
        self.response.write(start_template.render())

class BottleHandler(webapp2.RequestHandler):
    def get(self):
        bottle_template = jinja_env.get_template("glassbottle.html")

class LoginHandler(webapp2.RequestHandler):
    def post(self):
        login_template = jinja_env.get_template("Login/templates/login.html")



app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/login", LoginHandler)
], debug=True)

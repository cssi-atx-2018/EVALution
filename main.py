'''This python code creates the main page of our glass bottle website, loads in
the main page template, the glass bottle template'''

import webapp2
import os
import jinja2


jina_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("templates/mainpage.hmtl");

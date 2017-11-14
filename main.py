#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class AboutHandler(BaseHandler):
    def get(self):
        return self.render_template("O_meni.html")

class ProjectsHandler(BaseHandler):
    def get(self):
        return self.render_template("Moji_projekti.html")

class BlogHandler(BaseHandler):
    def get(self):
        sporocilo = "To je moje sporocilo"

        blog_posts = [{"title": "Prvi blog", "text": "test"}, {"title": "Drugi blog", "text": "test"}, {"title": "Tretji blog", "text": "test"}, {"title": "Cetrti blog", "text": "test"}]

        params = {"sporocilo": sporocilo, "blogs": blog_posts}

        return self.render_template("Blog.html", params=params)

class KontakHandler(BaseHandler):
    def get(self):
        return self.render_template("Kontakt.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/O_meni', AboutHandler),
    webapp2.Route('/Moji_projekti', ProjectsHandler),
    webapp2.Route('/Blog', BlogHandler),
    webapp2.Route('/Kontakt', KontakHandler),
], debug=True)

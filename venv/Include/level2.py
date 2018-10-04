import webapp2
import os


class MainPage(webapp2.RequestHandler):

    def render_template(self, filename, context={}):
        path = os.path.join(os.path.dirname(__file__), filename)
        self.response.out.write(webapp2.template.render(path, context))

    def get(self):
        self.render_template('index2.html')


application = webapp2.WSGIApplication([('.*', MainPage)], debug=False)

def main():
    from paste import httpserver
    httpserver.serve(application, host='127.0.0.1', port='8888')


if __name__ == '__main__':
    main()
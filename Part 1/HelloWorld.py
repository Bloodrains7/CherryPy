import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def helloWorld(self):
        return "Another hello world"


if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), '/')

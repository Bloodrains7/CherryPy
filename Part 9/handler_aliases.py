import cherrypy


class HandlerAlias(object):
    @cherrypy.expose(['index', 'home'])
    def index(self):
        return "Handler alias demo!"


if __name__ == '__main__':
    cherrypy.quickstart(HandlerAlias(), '/')

import cherrypy


class LogDemo(object):
    @cherrypy.expose
    def index(self):
        cherrypy.log('The index page was hit!')


if __name__ == '__main__':
    conf = {
        '/': {
            'log.access_file': '.\\accesslog.txt',
            'log.error_file': '.\\errorlog.txt',
            'log.screen': False
        }
    }
    cherrypy.quickstart(LogDemo(), '/', conf)

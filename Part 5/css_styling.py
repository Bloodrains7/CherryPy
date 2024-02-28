import os

import cherrypy


class Calculator(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

    @cherrypy.expose
    def result(self, a, b, manipulate):
        if manipulate == 'sum':
            result = float(a) + float(b)
        elif manipulate == 'multiply':
            result = float(a) * float(b)
        elif manipulate == 'divide':
            result = float(a) / float(b)
        else:
            result = float(a) - float(b)
        return '{} {} {} = {}'.format(a, manipulate, b, result)


if __name__ == '__main__':
    conf = {
        '/': {'tools.staticdir.root': os.path.abspath(os.getcwd())},
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '.\\public'
        }
    }
    cherrypy.quickstart(Calculator(), '/', conf)

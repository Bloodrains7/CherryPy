import cherrypy


class Calculator(object):
    @cherrypy.expose
    def index(self):
        return "Welcome to the calculator!"

    def sum(self, a, b):
        return ' a + b = {}'.format(float(a) + float(b))

    def multiply(self, a, b):
        return ' a * b = {}'.format(float(a) * float(b))

    def divide(self, a, b):
        return ' a / b = {}'.format(float(a) / float(b))

    def subtract(self, a, b):
        return ' a - b = {}'.format(float(a) - float(b))

    divide.exposed = True
    subtract.exposed = True
    multiply.exposed = True
    sum.exposed = True


if __name__ == '__main__':
    cherrypy.quickstart(Calculator(), '/')

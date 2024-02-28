import cherrypy


class JsonOut(object):
    @cherrypy.expose
    def index(self):
        return "Weekly menu!"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def menu(self):
        return {"weeklyMenu": {"monday": {}, "tuesday": {}, "wednesday": {}}}


if __name__ == "__main__":
    cherrypy.quickstart(JsonOut(), "/")

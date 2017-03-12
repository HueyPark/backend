from flask import Flask
from flask.views import MethodView
from flask_cors import CORS
from framework.world import Creater


class ApiServer:
    def __init__(self):
        self.__app = Flask('api_server')
        CORS(self.__app)

    def add_url_rule(self, rule: str, view: MethodView):
        self.__app.add_url_rule(rule, view_func=view.as_view(view.__qualname__))

    def run(self, host=None, port=None, debug=False):
        if debug is True:
            creater = Creater()
            creater.delete_nodes()
            creater.create_nodes()

        self.__app.run(host=host, port=port, debug=debug)

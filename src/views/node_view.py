from flask import jsonify
from flask.views import MethodView
from framework.database.models.node import Node
from framework.database.session import session
from typing import List


class NodeView(MethodView):
    methods = ['GET']

    def get(self):
        nodes = self.read_nodes()

        return jsonify({'nodes': list(map(lambda x: x.to_dict(), nodes))})

    def read_nodes(self)->List[Node]:
        return session.query(Node).all()

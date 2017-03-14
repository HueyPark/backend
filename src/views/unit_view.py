from flask import jsonify, request
from flask.views import MethodView
from framework.database.models.unit import Unit
from framework.database.session import session
from framework.id_generator import id_generator


class UnitView(MethodView):
    methods = ['POST']

    def post(self):
        node_id = request.json['node_id']

        unit = self.create_unit(node_id)

        return jsonify({'unit': unit.to_dict()})

    def create_unit(self, node_id)->Unit:
        unit = Unit(id_generator.generate(), node_id)
        session.add(unit)
        session.commit()

        return unit

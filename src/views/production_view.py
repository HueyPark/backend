from flask import jsonify
from flask.views import MethodView
from framework.database.models.production import Production
from framework.database.session import session
from framework.id_generator import id_generator
from typing import List


class ProductionView(MethodView):
    methods = ['GET', 'POST', 'DELETE']

    def post(self):
        production = self.create_production()

        production_dict = {
            'id': str(production.id),
            'create_time': production.create_time.timestamp(),
            'complete_time': production.complete_time.timestamp()}

        return jsonify({'production': production_dict})

    def get(self, production_id):
        if production_id is not None:
            production = self.read_production(production_id)
            production_dict = {
                'id': str(production.id),
                'create_time': production.create_time.timestamp(),
                'complete_time': production.complete_time.timestamp()}

            return jsonify({'production': production_dict})
        else:
            productions = []
            for production in self.read_productions():
                productions.append({
                    'id': str(production.id),
                    'create_time': production.create_time.timestamp(),
                    'complete_time': production.complete_time.timestamp()})

            return jsonify({'productions': productions})

    def delete(self, production_id):
        self.delete_production(production_id)

        return jsonify({'production_id': production_id})

    def create_production(self) -> Production:
        production = Production(id_generator.generate())
        session.add(production)
        session.commit()

        return production

    def read_production(self, production_id):
        production = session.query(Production).filter(Production.id == production_id).one_or_none()
        return production

    def read_productions(self) -> List[Production]:
        return session.query(Production).all()

    def delete_production(self, production_id):
        session.query(Production).filter(Production.id == production_id).delete()
        session.commit()

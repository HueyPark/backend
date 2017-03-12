from flask import jsonify
from flask import request
from framework.database.models.item import Item
from framework.database.models.production import Production
from framework.database.session import session
from framework.id_generator import id_generator


class ItemView:
    @classmethod
    def create_item(cls):
        item = cls._create_item(request.json)

        return jsonify({'item': item.to_dict()})

    @classmethod
    def read_items(cls):
        items = []
        for item in session.queyr(Item).all():
            items.append(item.to_dict())

        return jsonify({'items': items})

    @staticmethod
    def _create_item(json):
        production_id = json['production_id']

        result = session.query(Production).filter(Production.id == production_id).delete()
        if result != 1:
            raise Exception

        item = Item(id_generator.generate())
        session.add(item)
        session.commit()

        return item

    @staticmethod
    def _read_item(item_id):
        item = session.query(Item).filter(Item.id == item_id).one()
        return item

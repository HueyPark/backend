from .base import UnitBase


class Unit(UnitBase):
    def __init__(self, unit_id, node_id):
        self.id = unit_id
        self.node_id = node_id

    def to_dict(self):
        return {'id': str(self.id)}

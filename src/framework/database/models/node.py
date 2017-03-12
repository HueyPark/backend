from .base import NodeBase


class Node(NodeBase):
    def __init__(self, node_id, pos_x, pos_y):
        self.id = node_id
        self.pos_x = pos_x
        self.pos_y = pos_y

    def to_dict(self):
        return {'id': str(self.id), 'pos': {'x': self.pos_x, 'y': self.pos_y}}

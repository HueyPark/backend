from framework.database.models.node import Node
from framework.database.session import session
from framework.id_generator import id_generator
from random import randint


class Creater:
    def create_nodes(self):
        for _ in range(10):
            self.__create_random_node()

    def delete_nodes(self):
        session.query(Node).delete()
        session.commit()

    def __create_random_node(self):
        node = Node(id_generator.generate(), randint(0, 1000), randint(0, 1000))
        session.add(node)
        session.commit()

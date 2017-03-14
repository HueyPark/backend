from framework.database.models import Node, Unit
from framework.database.session import session
from framework.id_generator import id_generator


class Creater:
    def create_nodes(self):
        for x in range(5):
            for y in range(5):
                node = Node(id_generator.generate(), x * 100, y * 100)
                session.add(node)
        session.commit()

    def delete_nodes(self):
        session.query(Unit).delete()
        session.query(Node).delete()
        session.commit()

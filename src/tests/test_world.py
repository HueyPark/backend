from framework.world import Creater
from framework.database.utils import drop_and_create_all
from views import NodeView

drop_and_create_all()


class TestWorld:
    def test_create_world(self):
        creater = Creater()
        creater.create_nodes()

        node_view = NodeView()
        nodes = node_view.read_nodes()
        assert(len(nodes) != 0)

    def test_delete_world(self):
        creater = Creater()
        creater.delete_nodes()

        node_view = NodeView()
        nodes = node_view.read_nodes()
        assert(len(nodes) == 0)

from framework.database.utils import drop_and_create_all
from views import NodeView

drop_and_create_all()


class TestNodeView:
    def test_read_nodes(self):
        node_view = NodeView()
        node_view.read_nodes()

from framework.database.models.node import Node
from framework.database.session import session
from framework.database.utils import drop_and_create_all
from views import UnitView

drop_and_create_all()


class TestUnitView:
    def test_create_unit(self):
        node_id = 1
        node = Node(node_id, 0, 0)
        session.add(node)
        session.commit()

        unit_view = UnitView()
        unit_view.create_unit(node_id)

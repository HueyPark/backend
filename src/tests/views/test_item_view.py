from framework.database.utils import drop_and_create_all
from views import ItemView
from views import ProductionView

drop_and_create_all()


class TestItemView:
    def test_create_item(self):
        production_view = ProductionView()
        production = production_view.create_production()
        item = ItemView._create_item({'production_id': production.id})
        ItemView._read_item(item.id)

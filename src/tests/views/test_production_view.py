from framework.database.utils import drop_and_create_all
from views import ProductionView

drop_and_create_all()


class TestProductionView:
    def test_create_and_delete_production(self):
        production_view = ProductionView()
        production_created = production_view.create_production()
        production_readed = production_view.read_production(production_created.id)
        assert(production_created.id == production_readed.id)

        production_view.delete_production(production_created.id)
        production_readed = production_view.read_production(production_created.id)
        assert(production_readed is None)

    def test_read_productions(self):
        production_view = ProductionView()
        production_view.read_productions()

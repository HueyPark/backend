from framework.api_server import ApiServer
from views import NodeView, ProductionView

api_server = ApiServer()

api_server.add_url_rule('/nodes', NodeView)
api_server.add_url_rule('/productions', ProductionView)

api_server.run(port=5000, debug=True)

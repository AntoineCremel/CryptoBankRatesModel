from model import WorldModel
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule


liquidity_agent1_chart = ChartModule([{"Label" : "Agent1_liquidity",
					"Color": "Black"}],
					data_collector_name="datacollector")

deposit_agent1_chart = ChartModule([{"Label" : "Agent1_deposit",
					"Color": "Black"}],
					data_collector_name="datacollector")

liquidity_agent0_chart = ChartModule([{"Label" : "Bank liquidity",
					"Color": "Black"}],
					data_collector_name="datacollector")

server = ModularServer(WorldModel,\
	[liquidity_agent1_chart, deposit_agent1_chart, liquidity_agent0_chart],\
	"World model",
	{"n_agents": {"banks": 1, "households": 1}})

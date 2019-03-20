from model import WorldModel
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule


liquidity_agent1_chart = ChartModule([{"Label" : "Household liquidity",
					"Color": "Black"}],
					data_collector_name="datacollector")

deposit_agent1_chart = ChartModule([{"Label" : "Household deposit",
					"Color": "Black"}],
					data_collector_name="datacollector")

liquidity_agent0_chart = ChartModule([{"Label" : "Bank liquidity",
					"Color": "Black"}],
					data_collector_name="datacollector")

net_worth_agents_chart = ChartModule([{"Label": "Networth of household",
					"Color": "Black"},
					{"Label": "Networth of bank",
					"Color": "Red"}],
					data_collector_name="datacollector")

server = ModularServer(WorldModel,
	[net_worth_agents_chart, liquidity_agent0_chart],
	"World model",
	{"n_agents": {"banks": 1, "households": 200, "firms": 1}})

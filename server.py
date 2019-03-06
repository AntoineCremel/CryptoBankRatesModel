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

net_worth_agent1_chart = ChartModule([{"Label": "Networth of agent 1",
					"Color": "Black"}],
					data_collector_name="datacollector")

server = ModularServer(WorldModel,
	[net_worth_agent1_chart],
	"World model",
	{"n_agents": {"banks": 1, "households": 1}})

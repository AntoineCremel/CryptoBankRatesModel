from model import WorldModel
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule


liquidity_agent1_chart = ChartModule([{"Label" : "Agent1_liquidity",
					"Color": "Black"}],
					data_collector_name="datacollector")

server = ModularServer(WorldModel, [liquidity_agent1_chart], "World model",
	{"n_agents": {"banks": 1, "households": 1}})

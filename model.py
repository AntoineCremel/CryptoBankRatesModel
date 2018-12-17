from mesa import Model
from mesa.time import RandomActivation
from financeAgent import Household
from banks import Bank
from mesa.datacollection import DataCollector

class WorldModel(Model):
	"""
	The mesa class which runs our simulation
	"""
	def __init__(self, n_agents):
		"""
		Parameters
		n_agents : dict containing the number of each
			type of agents that we want our model to include
		"""
		self.n_banks = n_agents['banks']
		self.n_households = n_agents['households']
		# Chose a scheduler
		self.scheduler = RandomActivation(self)

		# Create the required number of each agent
		for i in range(self.n_banks):
			a = Bank(i, self)
			self.scheduler.add(a)

		for i in range(self.n_households):
			a = Household(i + n_banks, self)
			self.scheduler.add(a)

		# Create the data collector
		self.datacollector = DataCollector()

	def step(self):
		self.datacollector.collect(self)
		self.schedule.step()

from mesa import Model
from mesa.time import RandomActivation
from financeAgent import Household
from banks import Bank
from mesa.datacollection import DataCollector
from datetime import datetime, timedelta
import support_classes

class WorldModel(Model):
	"""
	The mesa class which runs our simulation
	"""

	def __init__(self, n_agents):
		"""
		Basic constructor with mostly default values

		Parameters
		n_agents : dict containing the number of each
			type of agents that we want our model to include
		"""
		# "Private parameters"
		# These parameters will be used to communicate to the agents that 
		# a new day or a new month started
		self.daypassed = False
		self.monthpassed = False

		# Attributes related to time
		self.start_datetime = datetime(2005, 1, 1, 0, 0, 0, tzinfo=None)
		self.current_datetime = self.start_datetime
		self.step_interval = "month"

		self.n_banks = n_agents['banks']
		self.n_households = n_agents['households']

		# Chose a scheduler
		self.scheduler = RandomActivation(self)

		# Create the required number of each agent
		for i in range(self.n_banks):
			a = Bank(i, self)
			self.scheduler.add(a)

		for i in range(self.n_households):
			a = Household(i + self.n_banks, self)
			self.scheduler.add(a)

		# Create the data collector
		self.datacollector = DataCollector(
			model_reporters = {"Agent1_liquidity": agent1_liquidity,
							"Agent1_deposit": agent1_deposit})

		self.running = True

	def time_tick(self, before_datetime):
		if before_datetime.day != self.current_datetime.day:
			self.daypassed = True
		else:
			self.daypassed = False

		if before_datetime.month != self.current_datetime.month:
			self.monthpassed = True
		else:
			self.monthpassed = False

	def step(self):
		"""
		One step represents one hour of time
		"""
		before_datetime = self.current_datetime
		# Update the current_datetime
		self.current_datetime = support_classes.addMonth(self.current_datetime)
		# Check if a new day passed
		self.time_tick(before_datetime)

		# Take the steps in the model
		self.datacollector.collect(self)
		self.scheduler.step()

def agent1_liquidity(model):
	return model.scheduler.agents[1].liquidity

def agent1_deposit(model):
	return model.scheduler.agents[1].deposit


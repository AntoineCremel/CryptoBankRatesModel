from mesa import Model
from mesa.time import RandomActivation
from household import Household
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
		self.n_firms = n_agents['firms']
		self.n_households = n_agents['households']

		# Chose a scheduler
		self.scheduler = RandomActivation(self)

		# Create the required number of each agent
		for i in range(self.n_banks):
			a = Bank(i, self)
			a.liquidity = 1000
			self.scheduler.add(a)

		for i in range(self.n_firms):
			a = Firm(i + self.n_banks, self)
			self.scheduler.add(a)

		for i in range(self.n_households):
			a = Household(i + self.n_banks + self.n_firms, self)
			self.scheduler.add(a)

		# If any deposits is to be given to banks it should be given now

		# Create the data collector
		self.datacollector = DataCollector(
			model_reporters = {"Household liquidity": agent1_liquidity,
							"Household deposit": agent1_deposit,
							"Bank liquidity": agent0_liquidity,
							"Networth of household": agent1_netWorth,
							"Networth of bank": agent0_netWorth})

		self.running = True


	def __getattr__(self, name):
		if name == "range_households":
			# This function returns a list with 2 numbers : the number of the
			# first household in the list, and the number of the last household in the list
			return range(n_banks + n_firms, n_banks + n_firms + n_households - 1)
		elif name == "range_firms":
			return range(n_banks, n_banks + n_firms - 1)

		elif name == "list_unemployed":
			# Return a list containing the ids of all the employees who do not have
			# a job
			unemployed = []
			# Make a for that runs through the agents
			for h_id in self.range_households:
				# Check if that agent doth or doth not have a job
				# by looping through the firms and checking their list of employees
				for f_id in self.range_firms:
					#for emp, sal in self.scheduler.agents[f_id].salary
					pass

		else:
			super().__getattr__(name)

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


# Those functions are used to create graphs for the model
def agent1_liquidity(model):
	return model.scheduler.agents[1].liquidity

def agent1_deposit(model):
	return model.scheduler.agents[1].deposit

def agent0_liquidity(model):
	return model.scheduler.agents[0].liquidity

def agent1_netWorth(model):
	return model.scheduler.agents[1].net_worth

def agent0_netWorth(model):
	return model.scheduler.agents[0].net_worth

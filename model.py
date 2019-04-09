from mesa import Model
from mesa.time import RandomActivation
from household import Household
from banks import Bank
from firms import Firm
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
		# Init all firms with their employees
		self.init_all_firms()

		# Create the data collector
		self.datacollector = DataCollector(
			model_reporters = {"Household liquidity": agent2_liquidity,
							"Household deposit": agent2_deposit,
							"Bank liquidity": agent0_liquidity,
							"Networth of household": agent2_netWorth,
							"Networth of bank": agent0_netWorth})

		self.running = True

	def init_all_firms(self, proportion_unemployed=0):
		"""
		This function is designed to be called inside the constructor.
		It runs through all the firms and initialises them
		"""
		nb_unemployed = len(self.list_unemployed)
		nb_ppl_available_for_hire = nb_unemployed * (1 - proportion_unemployed)
		for i in self.range_firms:
			# Determine how many people this firm is allowed to hire 
			# May add some randomness in here
			will_hire = len(list(self.range_households)) / len(list(self.range_firms))

			self.scheduler.agents[i].init(will_hire)


	def __getattr__(self, name):
		if name == "range_households":
			# This function returns a list with 2 numbers : the number of the
			# first household in the list, and the number of the last household in the list
			return range(self.n_banks + self.n_firms, self.n_banks + self.n_firms + self.n_households - 1)
		elif name == "range_firms":
			return range(self.n_banks, self.n_banks + self.n_firms - 1)

		elif name == "list_unemployed":
			# Return a list containing the ids of all the employees who do not have
			# a job

			# This dictionary contains, for each household, the list of household it contains that
			# does have a job
			employed = dict.fromkeys(list(self.range_households), 0)

			# Check how many jobs each household has
			for f_id in self.range_firms:
				for emp, __ in self.scheduler.agents[f_id].salaries.items:
					employed[emp] += 1

			# Then we loop through that dictionary, and for each household we add all
			# of the remaining adults to the output list
			unemployed = []
			for household, number in employed.items():
				unemployed_adults = self.scheduler.agents[household].n_adults - number
				for i in range(unemployed_adults):
					unemployed.append(household)

			return unemployed

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
def agent2_liquidity(model):
	return model.scheduler.agents[2].liquidity

def agent2_deposit(model):
	return model.scheduler.agents[2].deposit

def agent0_liquidity(model):
	return model.scheduler.agents[0].liquidity

def agent2_netWorth(model):
	return model.scheduler.agents[2].net_worth

def agent0_netWorth(model):
	return model.scheduler.agents[0].net_worth

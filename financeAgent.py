"""
Define the main class from which all agents will inherit

Each possible agent will come from this one
We assume only banks can give loans
"""
from mesa import Agent, Model
import random

class FinanceAgent(Agent):
	def __init__(self, unique_id, model):
		"""Basic definition of the init function
		
		This function lists all of the attributes of
		the agents and initializes them to 0
		"""
		# The parent class is mesa.Agent
		super().__init__(unique_id, model)

		self.liquidity = 0 # Available cash
		self.debt = 0 # Sum of money borrowed

	def step(self):
		"""
		This function will implement what the agent will do on
		each step of the simulation.
		"""
		pass

class Household(FinanceAgent):
	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)

		# "Private" internal attributes
		self.hours_worked_today = 0
		self.hours_worked_this_month = 0

		# Unique Id of the bank to which belongs
		self.bank_n = random.randint(0, model.n_banks-1)

		self.deposit = 1000
		self.n_work_hours_expected = 0
		self.hour_wage = 10
		self.n_adults = 1 #Number of adults capable of working

	def step(self):
		"""
		This function defines what a household will do on each
		step
		"""
		# If the household still wants to work, add work hours
		if self.hours_worked_today < self.n_work_hours_expected:
			# Increment amount of worked hours
			self.work_an_hour()

		if self.model.monthpassed:
			# Receive salary
			self.hours_worked_this_month = 0
		if self.model.daypassed:
			# Reset every daily value
			self.hours_worked_today = 0

	# Helper functions
	def work_an_hour(self):
		self.hours_worked_today += self.n_adults
		self.hours_worked_this_month += self.n_adults

	def get_account(self, bank):
		"""
		Return how much money this household has in bank n_bank
		"""
		if bank == self.bank_n:
			return self.deposit

	def change_account(self, bank, amount, overdraft_allowed=False):
		"""
		Withdraw or add money to the account of this household with this bank.
		"""
		if bank != self.bank_n:
			raise AttributeError("Having accounts in several different banks\
				is not implemented")

		# Check that the client has enough
		if amount < 0 and -amount > self.deposit and !overdraft_allowed:
			raise ValueError("Overdraft is not allowed")

		self.deposit += amount

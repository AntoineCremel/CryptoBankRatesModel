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
		self.deposit = 0

		# Unique Id of the bank to which belongs
		self.bank_n = random.randint(0, model.n_banks-1)

	def step(self):
		"""
		This function will implement what the agent will do on
		each step of the simulation.
		"""
		pass

	def setDeposit(self, new_deposit):
		"""
		This function is used to change the amount of money this agent has
		deposited on his bank account
		"""
		self.model.scheduler.agents[self.bank_n].liquidity +=\
			new_deposit - self.deposit
		self.deposit = new_deposit

	def addDeposit(self, amount):
		self.setDeposit(self.deposit + amount)

class Household(FinanceAgent):
	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)

		# "Private" internal attributes
		self.hours_worked_today = 0
		self.hours_worked_this_month = 0

		self.n_work_hours_expected = 35
		self.hour_wage = 10
		self.n_adults = 1 #Number of adults capable of working in the household
		self.setDeposit(1000)

	def step(self):
		"""
		This function defines what a household will do on each
		step
		"""
		# For now we consider that each household does exactly as many
		# work hours as it expects every month.
		self.hours_worked_this_month = self.n_work_hours_expected

		self.receive_salary()

		if self.model.monthpassed:
			# Receive salary
			self.hours_worked_this_month = 0
		if self.model.daypassed:
			# Reset every daily value
			self.hours_worked_today = 0

	# Helper functions
	def get_account(self, bank):
		"""
		Return how much money this household has in bank n_bank
		"""
		if bank == self.bank_n:
			return self.deposit

	def charge_account(self, bank, amount, overdraft_allowed=False):
		"""
		Withdraw or add money to the account of this household with this bank.
		"""
		if bank != self.bank_n:
			raise AttributeError("Having accounts in several different banks\
				is not implemented")

		# Check that the client has enough
		if amount < 0 and -amount > self.deposit and not overdraft_allowed:
			raise ValueError("Overdraft is not allowed")

		addDeposit(-1 * amount)

	def receive_salary(self):
		"""
		"""
		if self.model.monthpassed:
			self.addDeposit(self.hours_worked_this_month * self.hour_wage)


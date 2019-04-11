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

		# Unique Id of the bank to which belongs
		self.bank_n = random.randint(0, model.n_banks-1)
		self.deposit = 0
		self.liquidity = 0 # Available cash
		self.debt = 0 # Sum of money borrowed
		self.tangible_assets = 0 # Value of the tangible assets

	def __setattr__(self, name, value):
		"""
		This method will contain any special rule to modify attributes
		of an attribute
		"""
		# We add a special rule for deposit
		# this way anybody trying to modify deposit of finance agent
		# will also modify the liquidity of the bank of finance agent
		if name == "deposit":
			if value < 0:
				raise ValueError("Overdraft not allowed")
			try:
				self.model.scheduler.agents[self.bank_n].liquidity\
					+= value - self.deposit

				object.__setattr__(self, name, value)

			except IndexError:
				# If the bank has not been defined yet, we have to set the 
				# attribute to 0, because otherwise this agent would have
				# a deposit that is not contained in any banks liquidity
				print("Agent {} has no bank yet. Defaulting his deposit to 0.".format(self.unique_id))
				object.__setattr__(self, name, 0)
				pass

			except AttributeError:
				self.model.scheduler.agents[self.bank_n].liquidity\
					+= value
				object.__setattr__(self, name, value)
		else:
			object.__setattr__(self, name, value)

	def __getattr__(self, name):
		"""
		This method will contain all of the special indicators that are 
		a function of other attributes
		"""
		if name == "bank":
			# This variable contains a pointer towards the bank
			return self.model.scheduler.agents[self.bank_n]
		elif name == "debts":
			# loans contracted is the sum of all of the money this agent
			#### IN THIS VERSION WE CONSIDER PEOPLE CAN ONLY HAVE DEBTS
			# WITH THEIR MAIN BANK
			total_debt = 0

			#### Part that we have to modify once mensuality is implemented
			for loan in self.bank.loans:
				if loan.debtor == self.unique_id:
					total_debt += loan.value + loan.value * loan.interest_rate
			return total_debt

		elif name == "net_worth":
			return self.liquidity + self.tangible_assets + self.deposit

		elif name == "agents":
			return self.model.scheduler.agents

		else :
			# If name is not one of the variable that we are trying to
			# find then call the __getattr__ function of the mother class
			#super().__getattr__(name)
			raise AttributeError

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

	# Helper functions
	def get_account(self, bank):
		"""
		Return how much money this household has in bank n_bank
		"""
		if bank == self.bank_n:
			return self.deposit

	def charge_account(self, amount, overdraft_allowed=False, bank=-1):
		"""
		Withdraw or add money to the account of this household with this bank.
		"""
		if bank != self.bank_n and bank != -1:
			raise AttributeError("Having accounts in several different banks\
				is not implemented")

		# Check that the client has enough
		if amount > 0 and amount > self.deposit and not overdraft_allowed:
			raise ValueError("Overdraft is not allowed")

		self.deposit -= amount

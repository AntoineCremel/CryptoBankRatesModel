"""
Define the main class from which all agents will inherit

Each possible agent will come from this one
"""
from mesa import Agent, Model
from support_classes import Loan

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
		self.loans = [] # Array of loans given

	def step(self):
		"""
		This function will implement what the agent will do on
		each step of the simulation.
		"""
		self.payLoans()

	def payLoans(self):
		"""
		This function implements the payment of the regular due of
		the loan by self
		"""
		pass


class Household(FinanceAgent):
	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)

		# Unique Id of the bank to which belongs
		self.bank = 0
		self.deposit = 0

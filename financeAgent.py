"""
Define the main class from which all agents will inherit

Each possible agent will come from this one
"""
from mesa import Agent, Model
from support_classes import Loan
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
		self.loans = [] # Array of loans given

	def step(self):
		"""
		This function will implement what the agent will do on
		each step of the simulation.
		"""
		if self.model.monthpassed:
			self.payLoans()

	def payLoans(self):
		"""
		This function implements the payment of the regular due of
		the loan by self
		"""
		# This function will read all the loans of self to trigger payment
		# of monthly dues
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
		self.n_adults = 1

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
		self.hours_worked_today += 1
		self.hours_worked_this_month += 1

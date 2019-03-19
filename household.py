"""
This file contains the definition of household.
"""
from financeAgent import FinanceAgent
from support_classes import Loan

class Household(FinanceAgent):
	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)

		# "Private" internal attributes
		self.hours_worked_today = 0
		self.hours_worked_this_month = 0

		self.n_work_hours_expected = 150
		self.hour_wage = 3.75
		self.n_adults = 1 #Number of adults capable of working in the household
		self.deposit = 1000
		self.price_of_life = 100 # Price of basic standard monthly consumption

	def step(self):
		"""
		This function defines what a household will do on each
		step
		"""
		# For now we consider that each household does exactly as many
		# work hours as it expects every month.
		self.hours_worked_this_month = self.n_work_hours_expected

		self.receive_salary()
		self.monthly_consumption()

		if self.model.monthpassed:
			# Receive salary
			self.hours_worked_this_month = 0

	def receive_salary(self):
		"""
		"""
		if self.model.monthpassed:
			self.deposit += self.hours_worked_this_month * self.hour_wage

	def monthly_consumption(self):
		"""
		Implements the daily needs of the household for things like food
		and electricity.
		"""
		# For this first version we will consider only a fixed expenditure each month
		# later on, we will need to connect the consumption of a household with the
		# income of production firms.
		self.deposit -= self.price_of_life

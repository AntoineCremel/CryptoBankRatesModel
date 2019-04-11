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

		self.monthly_wage = 500 # Variable to store the amount received as wage this month
		self.n_adults = 1 #Number of adults capable of working in the household
		self.deposit = 1000
		self.price_of_life = 100 # Price of basic standard monthly consumption
		self.consumption_rate = 0.8 # Proportion of the wage this household spends each month
		#self.alpha1 = 0.6 # Propensity to consume out of income
		#self.alpha2 = 0.4 # Propensity to consume out of wealth
        

	def step(self):
		"""
		This function defines what a household will do on each
		step
		"""
		# For now we consider that each household does exactly as many
		# work hours as it expects every month.
		#self.hours_worked_this_month = self.n_work_hours_expected

		self.monthly_consumption()
		
		if self.model.monthpassed:
			# Receive salary
			self.hours_worked_this_month = 0


	def receive_salary(self, wage):
		"""
		A modifier
		"""
		self.deposit += wage
		self.monthly_wage = wage

	def monthly_consumption(self):
		"""
		Implements the daily needs of the household for things like food
		and electricity.
		"""
		# For this first version we will consider only a fixed expenditure each month
		# later on, we will need to connect the consumption of a household with the
		# income of production firms.
		consumption = self.monthly_wage * self.consumption_rate
		# Our consumption has to come from somewhere, so we give some money to a random asortment
		# of firms each months depending on our needs
		### ATTENTION : this first version only functions with one firm
		for i in self.model.range_firms:
			self.deposit -= consumption
			self.agents[i].liquidity += consumption
			consumption = 0

	def consumption(self) :
		"""
		Households consume out of their disposable income 
		"""
		self.disposable_income = self.deposit - self.price_of_life

	def consumption_demand(self) :  
		"""
		Consumption goods demand by household
		"""
		self.consumptiond = self.alpha1 * self.disposable_income + self.alpha2 * self.deposit

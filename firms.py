"""
This file contains the definition of 
the class for firms
"""

from financeAgent import FinanceAgent

class Firm(FinanceAgent):
	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)

		self.employees = [] # list of numbers indicating employees to the firm
		self.salaries = [] # list of salaries
		self.deposit = 10000
		### To complete : constructor of class firm

	def step(self):
		"""
		This function calls all the functions that should be executed each month
		"""
		self.give_salaries()

	def give_salaries(self):
		"""
		This function should give salaries to all the employees of the company
		"""
		pass # Take off the word pass when completing the function

	def produce_goods(self):
		"""
		This function will generate consumption goods wchich can be bought
		by households directly.
		"""
		pass

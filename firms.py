"""
This file contains the definition of 
the class for firms
"""

from financeAgent import FinanceAgent
import random

class Firm(FinanceAgent):
	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)

		self.salary_grid = [1200,1350,1500,1650,1800,2000,2300,2750,3600,5000] #Grid of salary
		self.salaries = {} # dictionary with as key numero of employe and as value salary
		self.deposit = 10000
		### To complete : constructor of class firm

	def init(self, nb_emp):
		list_unemployed = self.model.list_unemployed
		for i in range(nb_emp):
			emp_to_hire = random.randint(0,len(list_unemployed)-1)
			self.salaries[list_unemployed[emp_to_hire]] = self.salary_grid[random.randint(0, 9)]
			list_unemployed.pop(emp_to_hire)
			
			

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

	def give_dividends(self):
		"""
		This function will give dividends to all bank who have share
		"""
		pass #Take of the word pass when completing the function
		

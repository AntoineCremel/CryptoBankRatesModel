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
		self.efficiency = 1.4
		self.production = 0

	def init(self, nb_emp):
		"""
		This function takes as input nb_emp. It goes through the list of unemployed households,
		and hires up to nb_emp or the number of unemployed left, whichever is smaller. It then
		exits and returns the number of employees it could hire 
		"""
		list_unemployed = self.model.list_unemployed
		for i in range(nb_emp):
			if list_unemployed == []:
				return i
			emp_to_hire = random.randint(0,len(list_unemployed)-1)
			self.salaries[list_unemployed[emp_to_hire]] = self.salary_grid[random.randint(0, 9)]
			list_unemployed.pop(emp_to_hire)
			
		return nb_emp

	def step(self):
		"""
		This function calls all the functions that should be executed each month
		"""
		self.give_salaries()
		self.give_dividends()

	def give_salaries(self):
		"""
		This function should give salaries to all the employees of the company
		"""
		# Reset production
		self.production = 0

		for emp, salary in self.salaries.items():
			self.liquidity -= salary
			self.agents[emp].receive_salary(salary)
			# Add the salary to the amount of production
			self.production += efficiency * salary

	def give_dividends(self):
		"""
		This function will give dividends to all bank who have share
		"""
		pass #Take of the word pass when completing the function

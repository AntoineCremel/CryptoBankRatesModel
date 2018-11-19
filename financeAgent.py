"""
Define the main class from which all agents will inherit

Each possible agent will come from this one
"""
from mesa import Agent
from support_classes import Loan

class Agent():
	def __init__(self):
		"""Basic definition of the init function
		
		This function lists all of the attributes of
		the agents and initializes them to 0
		"""
		self.capital = 0
		self.extended_loans = 0
		self.debt = 0
		self.loans = [] # Array of loans

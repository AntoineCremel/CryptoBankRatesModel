"""
This file will contain the definition of all
of the banking classes
"""
from mesa import Agent
from financeAgent import FinanceAgent

class Bank(FinanceAgent):
	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)

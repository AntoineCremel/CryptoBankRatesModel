"""
This file will contain the definition of all
of the banking classes
"""
from mesa import Agent
from financeAgent import FinanceAgent, Household
from support_classes import Loan
import inspect

class Bank(FinanceAgent):
	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)
		self.loans = [] # Array of loans given

	def step(self):
		"""
		Implement the steps taken by the bank each turn
		"""
		# Payment of the loans is only checked once per month
		if self.model.monthpassed:
			self.get_loan_payments()

	def give_loan(self, start_date, end_date,
				debtor, interest_rate, value, loan_type):

		a = Loan(start_date, end_date, debtor,
				interest_rate, value, loan_type)

		self.loans.add(a)

	def get_loan_payments(self):
		"""
		This function will run through every loan on the list
		of loans, and ask debtors for payment of the appropriate
		amount

		"""
		# List containing all of the loans to delete 
		loans_to_delete = []

		for loan in self.loans:
			# Find the amount due
			due, debtor, end = loan.get_payment(self.model.current_date_time)
			# Check that any amount of money is due
			if not due:
				return
			# If the debtor is a household
			#if isinstance(self.model.scheduler.agents[debtor], Household):
			try:
				self.model.scheduler.agents[debtor].charge_account(self.unique_id, due, True)
				# Give liquidity to the bank
				self.liquidity += due
				# If the loan if fully repaid, delete it
				loans_to_delete.add(loan)
			except :
				# Couldn't withdraw for some reason, try to get from Household liquidity
				if self.model.scheduler.agents[debtor].liquidity >= due:
					self.model.scheduler.agents[debtor].liquidity -= due

				# Otherwise make a new loan
				else:
					raise Exception("Trying to get a household to repay a lona they can't afford.\n"+
						"Not implemented")

		for loan in loans_to_delete:
			self.loans.remove(loan)

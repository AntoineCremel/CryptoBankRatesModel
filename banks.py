"""
This file will contain the definition of all
of the banking classes
"""
from financeAgent import FinanceAgent
from support_classes import Loan

class Bank(FinanceAgent):
	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)
		self.loans = [] # Array of loans given

	def __getattr__(self, name):
		"""
		Contains the definition of attributes which are dinamically represented
		"""
		if name == "total_loaned":
			### Wait for REDA's work on loans
			### the current function is not compatible with mensualities
			total_loaned = 0
			for loan in self.loans:
				totatl_loaned += loan.value + loan.value * loan.interest_rate

			return total_loaned

		if name == "net_worth":
			"""
			For banks, we consider that deposit made into them is negative to the total
			networh cf Monetary Economics Table 2.4
			"""
			total_deposits = 0
			for agent in self.model.scheduler.agents :
				if agent.bank_n == self.unique_id:
					# If the bank number of the agent is equal to the id
					# of this bank, then the deposits of this agent is contained in
					# this bank
					total_deposits += agent.deposits

			return self.liquidity - total_deposits + self.total_loaned
		else:
			super().__getattr__(name)

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

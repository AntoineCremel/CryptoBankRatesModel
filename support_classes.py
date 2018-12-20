"""
Define the support classes needed in this program
"""
import datetime

class Loan():
	"""
	The class loan will hold data concerning a loan 
	given by one agent to another agent.


	"""
	def __init__(self, start_date, end_date,
				 debtor, interest_rate, value, loan_type="basic"):
		# Start by checking the compatibility of the parameters
		self.start_date = start_date
		self.end_date = end_date
		self.debtor = debtor
		self.interest_rate = interest_rate # in percentage
		self.value = value
		self.type = loan_type

	def get_payment(self, current_date):
		"""
		This function will return hoow much money is due for this month

		Return : amount of money due, debtor and end.
			- Amount of money due is the amount the debtor should pay to
			the owner of the loan
			- Debtor is the number of the agent who should pay this amount
			- end is a boolean which says wether or not this loan can be deleted
				from the database
		"""
		if self.type == "basic":
			"""
			In the case of a basic loan, everything is paid at once at
			the end date
			"""
			if current_date >= end_date:
				return value + (interest_rate/100) * value,\
					self.debtor,\
					self.true

			else:
				return None, None, False

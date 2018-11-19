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
				 debtor, interest_rate, value):
		# Start by checking the compatibility of the parameters
		self.start_date = start_date
		self.end_date = end_date
		self.debtor = debtor
		self.interest_rate = interest_rate
		self.value = value

"""
Define the support classes needed in this program
"""
import datetime
import calendar

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


###### Helper functions ######
def addMonth(source, n_months=1):
	"""
	This function takes a datetime as input and returns a date n_months
	later than datetime
	"""
	month = source.month - 1 + n_months
	year = source.year + month // 12
	month = month % 12 + 1
	day = min(source.day, calendar.monthrange(year, month)[1])
	return datetime.date(year, month, day)

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
		self.interest_rate = interest_rate
		self.value = value
		self.type = loan_type
        self.nb_month = ((end_date.year - start_date.year)*12)+end_date.month - start_date.month 
        self.mensuality = value/nb_months + ((value/nb_month)*interest_rate)
        self.remaining_val_with_interest = mensuality*nb_month

    def __getattr__(self, name):
    	# Definition of dynamic variables
    	if name=="total_val":
    		return value + value * interest_rate

    	else:
    		super().__getattr__(name)

    def __setattr__(self, name, value):
    	pass
        

	def get_payment(self, current_date):
		"""
		This function will return hoow much money is due for this month

		Return : amount of money due, debtor and end.
			- Amount of money due is the amount the debtor should pay to
			the owner of the loan
            - 
			- Debtor is the number of the agent who should pay this amount
			- end is a boolean which says wether or not this loan can be deleted
				from the database
		"""
		if self.type == "basic":
            #if "verifier que 10% du montant de la variable value correspondant est egal ou superieur au salaire du houesehold qui contracte le pret"
			"""
			In the case of a basic loan, everything is paid at once at
			the end date
			"""
			if current_date >= end_date:
                
				return value + (interest_rate) * value,
					self.debtor,
					True

			
           
        if self.type == "household loan":
            while current_date <= end_date:
               
                    return self.remainig_val_with_interest -= mensuality
                           self.debtor,
                           False
                    
                else:   
                    
                    return self.remainig_val_with_interest,
                           self.debtor,
                           True
                    
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

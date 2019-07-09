import matplotlib
import pandas
import PySimpleGUI
from datetime import datetime
import pickle

# Create a simple database to store expenditure based on categories - can do a dictionary with key
# being category and value being cumulative spendings. May need to define a function that creates a 
# new dictionary for each month  

# {amount, category, optional message, date}
#entry boxes/ option list for each

# main functions:

# - log spendings
# - store spendings details
# - generate graphs 


# storage of spendings needs to be external to the script, otherwise it just gets refreshed 
# everytime the the app is started 
# use pickle module to pickle a dictionary

database = {}

def init_store():
    """ initialise a monthly storage for expenditure. Keep track of year."""
    month = datetime.now().month
    year = datetime.now().year
    database[(month, year)] = {}
    return


def log_spending(category, amount, date):
    """ Log spending details into storage.
    
    Parameters:
        category (str): the category of spending (e.g. food)
        amount (float): the amount of money spent
        date (tuple<str, str>): month and year of the purchase
    """
    if database.get(date).get(category):
        init_amount = database.get(date).get(category)
        database[date][category] = init_amount + amount


def view_category_spendings():
    """ View by category (histogram??) use matplotlib """
    pass

def view_monthly_spendings():
    """ View total spendings by date (month) (line chart??) use matplotlib"""
    pass

init_store()
log_spending("food")
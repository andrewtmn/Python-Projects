import matplotlib
import pandas
from datetime import datetime
import pickle
import tkinter as tk

# Create a simple database to store expenditure based on categories - can do a dictionary with key
# being category and value being cumulative spendings. May need to define a function that creates a 
# new dictionary for each month  

# {amount, category, date}
#entry boxes/ option list for each

# main functions:

# - log spendings
# - store spendings details
# - generate graphs 


# storage of spendings needs to be external to the script, otherwise it just gets refreshed 
# everytime the the app is started 
# use pickle module to pickle a dictionary


# database = {}

# # Store data (serialize)  do this on closing of window
# with open('filename.pickle', 'wb') as handle:
#     pickle.dump(database, handle, protocol=pickle.HIGHEST_PROTOCOL)

# # Load data (deserialize) do this when 
# with open('filename.pickle', 'rb') as handle:
#     unserialized_data = pickle.load(handle)

# print(your_data == unserialized_data)
database = {}

CATEGORIES = ('food', 'entertainment', 'fitness', 'rent', 'technology',)

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
    else:
        database[date][category] = amount


def view_category_spendings():
    """ View by category (histogram??) use matplotlib 
    
    Can either make it appear in root window or a pop-up window"""
    pass

def view_monthly_spendings():
    """ View total spendings by date (month) (line chart??) use matplotlib
    
    can either make it appear in root window or a pop-up window"""
    pass



def main():
    root = tk.Tk()
    root.wm_title("Expense Tracker")
    root.mainloop()

if __name__ == "__main__":
    main()
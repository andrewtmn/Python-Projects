import matplotlib
import pandas
from datetime import datetime
import pickle
import tkinter as tk
from tkinter import DoubleVar

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

# # Load data (deserialize) do this when initalising an expense tracker
# with open('filename.pickle', 'rb') as handle:
#     unserialized_data = pickle.load(handle)

# print(database == unserialized_data)
database = {}

CATEGORIES = ('food', 'entertainment', 'fitness', 'rent', 'technology',)


class ExpenseTracker():
    """ A basic gui of an expense tracker. Log categorised spendings and view time-based/categorised
        expenditure."""

    def __init__(self, master):
        """ Constructor of an expense tracker"""
        # self._store = data_store
        self._master = master

        # 
        self._food = DoubleVar()
        self._entertainment = DoubleVar()
        self._fitness = DoubleVar()
        self._rent = DoubleVar()
        self._shopping = DoubleVar()
        self._transport = DoubleVar()

        self._heading = tk.Label(master, text="Expense Tracker", font=11).pack(expand=True)
        self._subheading = tk.Label(master, text="This is a very basic tracker for general expenditure")\
            .pack(expand=True)

        #might want to put these widgets in a list so method can loop through when plotting graphs
        self._food_entry = tk.Entry(master, textvariable=self._food)\
            .pack(pady=10, padx=10, expand=True, fill=tk.X)

        self._entertainment_entry = tk.Entry(master, textvariable=self._entertainment)\
            .pack(pady=10, padx=10, expand=True, fill=tk.X)

        self._fitness_entry = tk.Entry(master, textvariable=self._fitness)\
            .pack(pady=10, padx=10, expand=True, fill=tk.X)

        self._rent_entry = tk.Entry(master, textvariable=self._rent)\
            .pack(pady=10, padx=10, expand=True, fill=tk.X)

        self._shopping_entry = tk.Entry(master, textvariable=self._shopping)\
            .pack(pady=10, padx=10, expand=True, fill=tk.X)

        self._transport_entry = tk.Entry(master, textvariable=self._transport)\
            .pack(pady=10, padx=10, expand=True, fill=tk.X)

        # button to log entered spendings into the database
        self._log = tk.Button(master, text="Log Spendings", command=self.log_spending).pack(pady=5)


    def init_store(self):
        """ initialise a monthly storage for expenditure. Keep track of year."""
        month = datetime.now().month
        year = datetime.now().year
        database[(month, year)] = {}
        return


    def log_spending(self):
        """ Log spending details into storage.

        Parameters:
            category (str): the category of spending (e.g. food)
            amount (float): the amount of money spent
            date (tuple<str, str>): month and year of the purchase
        """
        month = datetime.now().month
        year = datetime.now().year
        date = (month, year,)

        for category in CATEGORIES:
            if database.get(date).get(category):
                init_amount = database.get(date).get(category)
                database[date][category] = init_amount + amount
            else:
                database[date][category] = amount


    def view_category_spendings(self):
        """ View by category (histogram??) use matplotlib 

        Can either make it appear in root window or a pop-up window"""
        pass

    def view_monthly_spendings(self):
        """ View total spendings by date (month) (line chart??) use matplotlib

        can either make it appear in root window or a pop-up window"""
        pass



def main():
    root = tk.Tk()
    root.wm_title("Expense Tracker")
    root.minsize(400,300)
    expense_tracker=ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
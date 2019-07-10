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


class ExpenseTracker(object):
    """ A basic gui of an expense tracker. Log categorised spendings and view time-based/categorised
        expenditure."""

    def __init__(self, master):
        """ Constructor of an expense tracker"""
        # self._store = data_store
        self._master = master
        # 

        # initialise variables for entry widgets
        self._food = DoubleVar()
        self._entertainment = DoubleVar()
        self._fitness = DoubleVar()
        self._rent = DoubleVar()
        self._shopping = DoubleVar()
        self._transport = DoubleVar()

        # create containers for each category
        food_frame = tk.Frame(master)
        ent_frame = tk.Frame(master)
        fitness_frame = tk.Frame(master)
        rent_frame = tk.Frame(master)
        shop_frame = tk.Frame(master)
        transp_frame = tk.Frame(master)


        self._heading = tk.Label(master, text="Expense Tracker", font=11).pack(side=tk.TOP, expand=True)
        self._subheading = tk.Label(master, text="This is a very basic tracker for general expenditure")\
            .pack(side=tk.TOP, expand=True)

       
       # pack label and entry widgets into their corresponding frames/containers 
        food_lbl = tk.Label(food_frame, text="Food").pack(side=tk.LEFT)
        self._food_entry = tk.Entry(food_frame, textvariable=self._food)\
            .pack(side=tk.LEFT, pady=10, padx=10, expand=True, fill=tk.X)

        ent_lbl = tk.Label(ent_frame, text="Entertainment").pack(side=tk.LEFT)
        self._entertainment_entry = tk.Entry(ent_frame, textvariable=self._entertainment)\
            .pack(side=tk.LEFT, pady=10, padx=10, expand=True, fill=tk.X)

        fitness_lbl = tk.Label(fitness_frame, text="Fitness").pack(side=tk.LEFT)
        self._fitness_entry = tk.Entry(fitness_frame, textvariable=self._fitness)\
            .pack(side=tk.LEFT, pady=10, padx=10, expand=True, fill=tk.X)
        
        rent_lbl = tk.Label(rent_frame, text="Rent").pack(side=tk.LEFT)
        self._rent_entry = tk.Entry(rent_frame, textvariable=self._rent)\
            .pack(side=tk.LEFT, pady=10, padx=10, expand=True, fill=tk.X)
 
        shop_lbl = tk.Label(shop_frame, text="Shopping").pack(side=tk.LEFT)
        self._shopping_entry = tk.Entry(shop_frame, textvariable=self._shopping)\
            .pack(side=tk.LEFT, pady=10, padx=10, expand=True, fill=tk.X)
        
        transp_lbl = tk.Label(transp_frame, text="Transport").pack(side=tk.LEFT)
        self._transport_entry = tk.Entry(transp_frame, textvariable=self._transport)\
            .pack(side=tk.LEFT, pady=10, padx=10, expand=True, fill=tk.X)

        # pack containers into the master window
        food_frame.pack(side=tk.TOP)
        ent_frame.pack(side=tk.TOP)
        fitness_frame.pack(side=tk.TOP)
        rent_frame.pack(side=tk.TOP)
        shop_frame.pack(side=tk.TOP)
        transp_frame.pack(side=tk.TOP)

        # button to log entered spendings into the database
        self._log = tk.Button(master, text="Log Spendings", command=self.log_spending)\
            .pack(pady=5, padx=5, ipadx=8, side=tk.TOP)


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
            amount = getattr("_" + category).get()
            if self._database.get(date).get(category):
                init_amount = self._database.get(date).get(category)
                self._database[date][category] = init_amount + amount
            else:
                self._database[date][category] = amount


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
    root.title("Expense Tracker")
    root.minsize(400,300)
    expense_tracker=ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
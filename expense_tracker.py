
# import graphing tools
import matplotlib
from matplotlib import style
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np 

# haven't used this yet - need to read about it
import pandas

# for logging dates and its spendings
from datetime import datetime

#for storing data on expenditure
import pickle

import tkinter as tk
from tkinter import ttk
from tkinter import DoubleVar

from PIL import Image, ImageTk

# Create a simple database to store expenditure based on categories 

# {amount, category, date}
#entry boxes/ option list for each

# main functions:

# - log spendings
# - store spendings details in dictionary
# - generate graphs and update them

# storage of spendings needs to be external to the script, otherwise it just gets refreshed 
# everytime the the app is started 
# use pickle module to pickle a dictionary

#strucutre of database:  (dict<tuple:dict>)
# {(date):{'food':0, 'shopping':0, etc.}, ...}

CATEGORIES = ('food', 'entertainment', 'fitness', 'rent', 'transport', 'shopping')
UPPER_CATEG = ('Food', 'Entertainment', 'Fitness', 'Rent', 'Transport', 'Shopping')

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        # Every page inherits the pickled dictionary
        self._database = {}
        self._load_database()

    def show(self):
        self.lift()

    # Every page has the dictionary loaded as an instance of itself
    def _load_database(self):
        """ Loads persistent storage containing information about expenditure."""
        with open('expense_tracker.pickle', 'rb') as handle:
            self._database = pickle.load(handle)


class LogSpendings(Page):
    """ Page providing ability for user to log spendings into the persistent storage. Spendings are
    stored by the month in a dictionary."""

    def __init__(self, *args, **kwargs ):
        """ Constructor """
        Page.__init__(self, *args, **kwargs)
        
        self._init_vars()
        self._init_frames()
        self._init_headings()
        self._init_labels()
        self._init_entries()
        button = tk.Button(self, text="print_data", command=self.print_data).pack(expand=True)
        button2 = tk.Button(self, text="clear data", command=self.clear_database).pack(expand=True)
        self._pack_frames()
        
        # button to log entered spendings into the database
        self._log = tk.Button(self, text="Log Spendings", command=self.log_spending)\
            .pack(pady=5, padx=5, ipadx=8, side=tk.TOP)

    def _init_vars(self):
        """ Initialise double variables for entry widgets"""
        # initialise variables for entry widgets
        self._food = DoubleVar()
        self._entertainment = DoubleVar()
        self._fitness = DoubleVar()
        self._rent = DoubleVar()
        self._shopping = DoubleVar()
        self._transport = DoubleVar()
        return
    
    def _init_frames(self):
        """ Initialise frames for each spending category"""
        # create containers for each category
        self._food_frame = tk.Frame(self)
        self._ent_frame = tk.Frame(self)
        self._fitness_frame = tk.Frame(self)
        self._rent_frame = tk.Frame(self)
        self._shop_frame = tk.Frame(self)
        self._transp_frame = tk.Frame(self)
        return

    def _init_headings(self):
        """ Initialise headings for the page"""
        # Headings for the app
        self._heading = tk.Label(self, text="Expense Tracker", font=11).pack(side=tk.TOP, expand=True)
        self._subheading = tk.Label(self, text="Enter your spendings and press 'Log Spendings'")\
            .pack(side=tk.TOP, expand=True)
        return
    
    def _pack_frames(self):
        """Pack frames (vertically stacked) into the page"""
        # pack containers into the master window
        self._food_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10)
        self._ent_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10)
        self._fitness_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10)
        self._rent_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10)
        self._shop_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10)
        self._transp_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10)
        return

    def _init_labels(self):
        """ Initialise labels for each category and pack"""
        self._food_lbl = tk.Label(self._food_frame, text="Food")\
            .pack(side=tk.LEFT, ipadx=28, padx=5, expand=True, anchor=tk.E)
        self._ent_lbl = tk.Label(self._ent_frame, text="Entertainment")\
            .pack(side=tk.LEFT, ipadx=4, padx=5, expand=True, anchor=tk.E)
        self._fitness_lbl = tk.Label(self._fitness_frame, text="Fitness")\
            .pack(side=tk.LEFT, ipadx=23, padx=5, expand=True, anchor=tk.E)
        self._rent_lbl = tk.Label(self._rent_frame, text="Rent")\
            .pack(side=tk.LEFT, ipadx=29, padx=5, expand=True, anchor=tk.E)
        self._shop_lbl = tk.Label(self._shop_frame, text="Shopping")\
            .pack(side=tk.LEFT, ipadx=16, padx=5, expand=True, anchor=tk.E)
        self._transp_lbl = tk.Label(self._transp_frame, text="Transport")\
            .pack(side=tk.LEFT, ipadx=16, padx=5, expand=True, anchor=tk.E)
        return

    def _init_entries(self):
        """ Initialise entry widgets for each category and pack"""
        self._food_entry = tk.Entry(self._food_frame, textvariable=self._food)\
            .pack(side=tk.RIGHT, pady=10, padx=10, expand=True, anchor=tk.W)
        self._entertainment_entry = tk.Entry(self._ent_frame, textvariable=self._entertainment)\
            .pack(side=tk.RIGHT, pady=10, padx=10, expand=True, anchor=tk.W)        
        self._fitness_entry = tk.Entry(self._fitness_frame, textvariable=self._fitness)\
            .pack(side=tk.RIGHT, pady=10, padx=10, expand=True, anchor=tk.W)      
        self._rent_entry = tk.Entry(self._rent_frame, textvariable=self._rent)\
            .pack(side=tk.RIGHT, pady=10, padx=10, expand=True, anchor=tk.W)       
        self._shopping_entry = tk.Entry(self._shop_frame, textvariable=self._shopping)\
            .pack(side=tk.RIGHT, pady=10, padx=10, expand=True, anchor=tk.W)       
        self._transport_entry = tk.Entry(self._transp_frame, textvariable=self._transport)\
            .pack(side=tk.RIGHT, pady=10, padx=10, expand=True, anchor=tk.W)
        return

# ------------------------------ DEBUGGING ---------------
    def print_data(self):
        """ This method is for debugging purposes only."""
        print(self._database.items())
        print(self._database.keys())
        print(self._database.values())
        return

    def clear_database(self):
        """Deletes all memory stored on database dictionary"""
        self._database = {}
        return
# --------------------------------------------------------
    
    def _save_database(self): # save log into persistent storage
        """ Saves current data on self._database to pickle file"""
        with open('expense_tracker.pickle', 'wb') as handle:
            pickle.dump(self._database, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return


    def log_spending(self):
        """ Retrieves entered spendings and logs the values into storage (self._database)."""
        # get current month and date (this is the key)
        month = datetime.now().month
        year = datetime.now().year
        date = (month, year,)

        # add date and/or category if not exists, else add to the current value stored in dict
        for category in CATEGORIES:
            amount = getattr(self, "_" + category).get()
            if self._database.get(date) is not None:
                if self._database.get(date).get(category) is not None:
                    init_amount = self._database.get(date).get(category)
                    self._database[date][category] = init_amount + amount
                else:
                    self._database[date][category] = amount
            else:
                self._database[date] = {}
                self._database[date][category] = amount
        
        print("Successfully saved log!")
        
        self._save_database()
        return


#might want to do a getter method that obtains the amount for each date

    # def view_category_spendings(self):
    #     """ View by category (histogram??) use matplotlib 

    #     Can either make it appear in root window or a pop-up window"""

    #     back_btn = tk.Button(self._master, text="Back to Main Page")
    #     pass

    # def view_monthly_spendings(self):
    #     """ View total spendings by date (month) (line chart??) use matplotlib

    #     can either make it appear in root window or a pop-up window"""
    #     back_btn = tk.Button(self._master, text="Back to Main Page")
    #     pass


class CategoryGraphs(Page):
    """ Page displaying current month's categorical spendings. """
    def __init__(self, *args, **kwargs ):
        """ Constructor of an expense tracker"""
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Spending Based On Category", font=12)\
            .pack(expand=True, anchor=tk.N, pady=8)

        f = Figure(figsize=(5,5), dpi=100)
        a= f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        create_graph = tk.Button(self, text="Update Graph").pack(expand=True, pady=5, anchor=tk.S)

    def _update_category_values(self):
        """ Retrieves current values for the month's categorical spendings."""
        (month, year,) = (datetime.now().month, datetime.now().year,)
        if self._database.get((month, year,)) is None:
            return
        for category in CATEGORIES:
            pass


        

class MonthlyGraphs(Page):
    """ Page displaying line graph of total spendings per month"""
    def __init__(self, *args, **kwargs ):
        """ Constructor """
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Monthly Spendings (Histogram)", font=12)\
            .pack(expand=True, anchor=tk.N, pady=8)

        self._monthly_values = []
        self._months = []
        self._init_graph()

        create_graph = tk.Button(self, text="Update Graph", command=self._update_graph)\
            .pack(expand=True, pady=5, anchor=tk.S)
        return

    def _init_graph(self):
        """ Updates the graph values to the current data stored in the dictionary. """
        # create figure and add subplot
        self._f = Figure(figsize=(3,3), dpi=100)
        self._a = self._f.add_subplot(111)

        self._update_plot_pts()
        self._a.plot(self._months, self._monthly_values, marker='o')

        self._canvas = FigureCanvasTkAgg(self._f, self)
        self._canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        return
    
    def _update_graph(self):
        """ Updates the set of points to plot and plots them on the figure """
        self._update_plot_pts()
        self._a.clear()
        self._a.plot(self._months, self._monthly_values, marker='o')
        return

    def _update_plot_pts(self):
        """ Retrieves current year's months and monthly spendings and stores them in lists."""
        curr_year = datetime.now().year
        self._monthly_values = []
        self._months = []

        for i in range(1, 13):
            if self._database.get((i, curr_year,)) is not None:
                self._monthly_values.append(sum(self._database.get((i, curr_year,)).values()))
                self._months.append(i)
        return



class PieGraph(Page):
    """ Page displaying pie chart of categorical spendings for the current month."""
    def __init__(self, *args, **kwargs ):
        """ Constructor """
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Monthly Spendings based on Category",font=12)\
            .pack(expand=True, anchor=tk.N, pady=8)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        create_graph = tk.Button(self, text="Update Chart").pack(expand=True, pady=5, anchor=tk.S)
        return



class Home(Page):
    """ Home page of application. """
    def __init__(self, *args, **kwargs ):
        """ Constructor """
        Page.__init__(self, *args, **kwargs)
        welcome = tk.Label(self, text="Welcome to the Expense Tracker App!", font=12)\
            .pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        load = Image.open("analytics-icon.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.pack(side=tk.TOP, expand=True)

        desc = tk.Label(self, text="Click on one of the buttons below to get started.")\
            .pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        return




class MainView(tk.Frame):
    """ Main view for user when application is run. Contains buttons that direct users to 
    different pages of the application."""

    def __init__(self, *args, **kwargs):
        """ constructor """
        tk.Frame.__init__(self, *args, **kwargs)

        self._init_pages()
        self._init_containers()
        self._place_pages()
        self._init_buttons()

        # show the home page first
        self._home.show()
        return

    def _init_pages(self):
        """ Initialise 'pages' (tk.Frame) for the application """
        # create instances of the frames I want to toggle
        self._home = Home(self)
        self._log = LogSpendings(self)
        self._category = CategoryGraphs(self)
        self._monthly = MonthlyGraphs(self)
        self._pie = PieGraph(self)
        return

    def _init_containers(self):
        """ Initialise the containers for buttons and pages."""
        # create containers for the buttons and frames
        self._buttonframe = tk.Frame(self)
        self._container = tk.Frame(self)
        self._buttonframe.pack(side=tk.TOP, fill=tk.X, expand=False)
        self._container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        return

    def _place_pages(self):
        """ Place the 'pages' into the container."""
        # place each 'page'/frame into the container
        self._home.place(in_=self._container, x=0, relwidth=1, relheight=1)
        self._log.place(in_=self._container, x=0, y=0, relwidth=1, relheight=1)
        self._category.place(in_=self._container, x=0, y=0, relwidth=1, relheight=1)
        self._monthly.place(in_=self._container, x=0, y=0, relwidth=1, relheight=1)
        self._pie.place(in_=self._container, x=0, y=0, relwidth=1, relheight=1)
        return

    def _init_buttons(self):
        """ Initialise buttons to toggle to different pages."""
        # buttons to toggle to the different pages
        self._log_btn = tk.Button(self, text="Log spendings", command=self._log.lift)\
            .pack(side=tk.LEFT, padx=5, pady=5, expand=True)
        self._category_btn = tk.Button(self, text="View category spending", \
            command=self._category.lift).pack(side=tk.LEFT, padx=5, pady=5, expand=True)
        self._month_btn = tk.Button(self, text="View monthly spending", command=self._monthly.lift)\
            .pack(side=tk.LEFT, padx=5, pady=5, expand=True)
        self._pie_btn = tk.Button(self, text="View Pie Chart", command=self._pie.lift)\
            .pack(side=tk.LEFT, padx=5, pady=5, expand=True)
        return
    




def main():
    root = tk.Tk()
    root.title("Expense Tracker")
    root.minsize(500,500)
    expense_tracker=MainView(root)
    expense_tracker.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()
import time 
import tkinter as tk
import winsound
import datetime
from tkinter import messagebox

class AlarmClock():
    """ Simple class that represents an alarm clock."""
    def __init__(self, master):
        """ Constructor of an alarm clock object. """

        self._master=master

        self._current_time = time.asctime(time.localtime(time.time()))

        # label showing the current time
        self._date_time = tk.Label(master, text=str(self._current_time), font=12)
        self._date_time.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        
        # Label showing the alarm time that was set by user
        self._time_set = tk.StringVar()
        self._alarm_time = tk.Label(master, font=10, text="Set your alarm in minutes", relief=tk.RAISED)
        self._alarm_time.pack(ipadx=5, ipady=5)

        # frame containing entry widget and reset/set buttons
        self._set_alarm_frame = tk.Frame(master)
        self._set_alarm_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        minutes_label = tk.Label(self._set_alarm_frame, text="Set Minutes for Alarm:")\
            .pack(side=tk.LEFT, expand=True, fill = tk.X, padx=5)

        self._alarm_entry = tk.Entry(self._set_alarm_frame, textvariable=self._time_set)
        self._alarm_entry.pack(side=tk.LEFT, expand=True, fill = tk.X)

        self._reset_alarm = tk.Button(self._set_alarm_frame, text="Reset Alarm", command=self.reset)
        self._reset_alarm.pack(side=tk.RIGHT, padx=5)

        self._set_alarm = tk.Button(self._set_alarm_frame, text="Set Alarm", command=self.set_time)
        self._set_alarm.pack(side=tk.RIGHT, padx=5)

        self.redraw()

    def redraw(self):
        """ Refreshes the current time clock so that time is updated every second """
        self._current_time = time.asctime(time.localtime(time.time()))
        self._date_time.config(text=str(self._current_time))

        # perform check if alarm time has been reached
        self.check_if_time()

        self._master.after(500, self.redraw)

    def set_time(self):
        """ Sets alarm time and renders it in the window"""
        try:
            mins = int(self._time_set.get())
            alarm_time = datetime.datetime.now() + datetime.timedelta(minutes=mins)
            self._alarm_time.config(text=str(alarm_time.ctime().__str__()))
        except: 
            self._alarm_time.config(text="That's not a valid value for minutes.")
            self._time_set.set(0)
        return
    

    def check_if_time(self):
        """ checks if alarm time has been reached; alerts user if that is the case"""
        if self._alarm_time["text"] == self._current_time:
            self.reset()
            messagebox.showinfo("Time is up", "Your alarm went off")
            
    
    def reset(self):
        """ Resets the alarm time """
        self._alarm_time.config(text="Set your alarm in minutes")
        self._time_set.set(0)

          

def main():
    root = tk.Tk()
    root.minsize(400,300)
    root.title("Alarm Clock")
    alarm = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()

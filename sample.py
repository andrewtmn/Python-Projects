
import tkinter as tk

class App():

    def __init__(self, master):

        frame1 = tk.Frame(master, height=100, width=100, bg="green")
        widget1 = tk.Label(frame1, text="Frame1").grid(row=0)
        widget1_1 = tk.Entry(frame1).grid(row=0, column=1)
        frame1.pack()

        frame2 = tk.Frame(master, height=1, width=100, bg="blue")
        widget2 = tk.Label(frame2, text="Frame2").grid(row=0)
        widget2_1 = tk.Entry(frame2).grid(row=0, column=1)
        frame2.pack()

        # frame3 = tk.Frame(master, height=100, width=100, bg="red").pack(side=tk.TOP)
        # widget3 = tk.Label(frame3, text="Frame3").pack()
        # widget3_1 = tk.Entry(frame3).pack()


def main():
    root = tk.Tk()
    root.title("testing")
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()

        
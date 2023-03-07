import tkinter as tk
from tkinter import ttk
import automation

class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("CAD labeling automation")
        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 5
        self.window['pady'] = 5

        # Number of rows
        self.num_rows_label = ttk.Label(self.window, text="Number of rows:")
        self.num_rows_label.grid(row=1, column=1, sticky=tk.W)

        self.num_rows_entry = ttk.Entry(self.window, width=5)
        self.num_rows_entry.grid(row=1, column=2, sticky=tk.W)
        self.num_rows_entry.insert(0, "5")

        # Number of columns
        self.num_cols_label = ttk.Label(self.window, text="Number of Columns:")
        self.num_cols_label.grid(row=2, column=1, sticky=tk.W)

        self.num_cols_entry = ttk.Entry(self.window, width=5)
        self.num_cols_entry.grid(row=2, column=2, sticky=tk.W)
        self.num_cols_entry.insert(0, "10")

        # Row spacing
        self.row_spacing_label = ttk.Label(self.window, text="row-spacing (mm):")
        self.row_spacing_label.grid(row=3, column=1, sticky=tk.W)

        self.row_spacing_entry = ttk.Entry(self.window, width=5)
        self.row_spacing_entry.grid(row=3, column=2, sticky=tk.W)
        self.row_spacing_entry.insert(0, "10")

        # Column spacing
        self.col_spacing_label = ttk.Label(self.window, text="column-spacing (mm):")
        self.col_spacing_label.grid(row=4, column=1, sticky=tk.W)

        self.col_spacing_entry = ttk.Entry(self.window, width=5)
        self.col_spacing_entry.grid(row=4, column=2, sticky=tk.W)
        self.col_spacing_entry.insert(0, "10")

        # Instructions
        self.instr = ttk.Label(self.window, text="Instructions:")
        self.instr.grid(row=5, column=1, columnspan=2, sticky=tk.W)

        self.instr_1 = ttk.Label(self.window, text="Put first label above top left sensor")
        self.instr_1.grid(row=6, column=1, columnspan=2, sticky=tk.W)

        self.instr_2 = ttk.Label(self.window, text="Have AutoCAD open and visible")
        self.instr_2.grid(row=7, column=1, columnspan=2, sticky=tk.W)

        self.instr_3 = ttk.Label(self.window, text="Click Start button")
        self.instr_3.grid(row=8, column=1, columnspan=2, sticky=tk.W)

        self.instr_4 = ttk.Label(self.window, text="Click top right of label and then bottom left")
        self.instr_4.grid(row=9, column=1, columnspan=2, sticky=tk.W)

        self.instr_5 = ttk.Label(self.window, text="Click num lock")
        self.instr_5.grid(row=10, column=1, columnspan=2, sticky=tk.W)

        # Start button
        self.start_button = ttk.Button(self.window, text="Start", command=self.start)
        self.start_button.grid(row=11, column=1, sticky=tk.W)

    def start(self):
        # Collects data from entry fields
        num_rows = self.num_rows_entry.get()
        num_cols = self.num_cols_entry.get()
        row_spacing = self.row_spacing_entry.get()
        col_spacing = self.col_spacing_entry.get()
        automation_init=automation.automation() # Initializes class
        automation_init.start(num_rows,num_cols,row_spacing,col_spacing) # Starts program

program = GUI()
program.window.mainloop()

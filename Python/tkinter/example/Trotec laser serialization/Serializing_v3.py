# Sheet Types: Gas Sensor, pH Sensor, Reference Electrode

import tkinter as tk
from tkinter import ttk
import Serializing_lib_v3

class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Serializing Laser File Generator")
        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 5
        self.window['pady'] = 5

        # Julian Date
        self.julian_label = ttk.Label(self.window, text = "Julian date:")
        self.julian_label.grid(row = 1, column = 1, sticky = tk.W)

        self.julian_entry = ttk.Entry(self.window, width = 10)
        self.julian_entry.grid(row = 1, column = 2, sticky = tk.W)
        self.julian_entry.insert(0, "B9001")

        # Sheet Type
        self.sheet_type_label = ttk.Label(self.window, text = "Sheet type:")
        self.sheet_type_label.grid(row = 2, column = 1, sticky = tk.W)

        self.sheet_type = ttk.Combobox(self.window, values = ['Gas Sensor', 'pH Sensor', 'Reference Electrode'])
        self.sheet_type.grid(row = 2, column = 2, sticky = tk.W)

        # Start sheet number
        self.sheet_start_label = ttk.Label(self.window, text = "Starting sheet number:")
        self.sheet_start_label.grid(row = 3, column = 1, sticky = tk.W)

        self.sheet_start_entry = ttk.Entry(self.window, width = 10)
        self.sheet_start_entry.grid(row = 3, column = 2, sticky = tk.W)
        self.sheet_start_entry.insert(0, "1")

        # Number of sheets
        self.num_sheet_label = ttk.Label(self.window, text = "Number of sheets:")
        self.num_sheet_label.grid(row = 4, column = 1, sticky = tk.W)

        self.num_sheet_entry = ttk.Entry(self.window, width = 10)
        self.num_sheet_entry.grid(row = 4, column = 2, sticky = tk.W)
        self.num_sheet_entry.insert(0, "10")

        # Start button
        self.start_button = ttk.Button(self.window, text = "Generate", command = self.start)
        self.start_button.grid(row = 5, column = 1, sticky = tk.W)

    def start(self):
        # Collects data from entry fields
        julian = self.julian_entry.get()
        sheet_type = self.sheet_type.get()
        sheet_start = self.sheet_start_entry.get()
        num_sheet = self.num_sheet_entry.get()
        Serializing_lib_v3.Serializing(julian, sheet_type, sheet_start, num_sheet) # Starts program

program = GUI()
program.window.mainloop()

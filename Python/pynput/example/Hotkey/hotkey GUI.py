import tkinter as tk
from tkinter import ttk
import hotkey

class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("CAD labeling hotkey")
        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 5
        self.window['pady'] = 5

        self.start_label = ttk.Label(self.window, text="Start label:")
        self.start_label.grid(row=1, column=1, sticky=tk.W)

        self.start_entry = ttk.Entry(self.window, width=5)
        self.start_entry.grid(row=1, column=2, sticky=tk.W)
        self.start_entry.insert(0, "A1")

        self.num_col_label = ttk.Label(self.window, text="Number of Columns:")
        self.num_col_label.grid(row=2, column=1, sticky=tk.W)

        self.num_col_entry = ttk.Entry(self.window, width=5)
        self.num_col_entry.grid(row=2, column=2, sticky=tk.W)
        self.num_col_entry.insert(0, "10")

        self.start_button = ttk.Button(self.window, text="Start", command=self.start)
        self.start_button.grid(row=3, column=1, sticky=tk.W)

        self.stop_button = ttk.Button(self.window, text="Stop",command=self.window.destroy)
        self.stop_button.grid(row=3, column=2, sticky=tk.W)
        self.stop_button.configure(state='disabled')

        self.instr_1 = ttk.Label(self.window, text="Select text using multiple mode")
        self.instr_1.grid(row=4, column=1, columnspan=2, sticky=tk.W)

        self.instr_2 = ttk.Label(self.window, text="Press num lock to insert label")
        self.instr_2.grid(row=5, column=1, columnspan=2, sticky=tk.W)

    def start(self):
        start_label = self.start_entry.get()
        num_col = self.num_col_entry.get()
        self.start_button.configure(state='disabled')
        self.stop_button.configure(state='enabled')
        hotkey_init=hotkey.hotkey()
        hotkey_init.start(start_label,num_col)


program = GUI()
program.window.mainloop()

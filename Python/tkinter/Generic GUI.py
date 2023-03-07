import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np
import time
import glob
import datetime
import platform
import csv

class Generic_GUI:
    def __init__(self,window):
        self.window = window # Main widget is the window

        def on_closing():
            """
            This will run when window is manually closed
            Good for closing ports and turning off instruments
            """
        
        self.window.protocol('WM_DELETELWINDOW',on_closing)
        self.window.title("Generic GUI")
        self.create_widgets() # Generate all other widgets

        # Initialize variables
        """
        Initialize variables here
        """
        self.max_graph=500 # Maximum number of points in the graphing window
        self.t=np.zeros((1,1)) # used to hold time data
        self.y_data=np.zeros((1,4)) # Adjust to hold y-data

        ### Generate widgets within window ###
    def create_widgets(self):
        self.window['padx'] = 5 # Slight padding of frames from edge of window
        self.window['pady'] = 5

        # - - - - -
        # Save File Frame
        sav_frame = ttk.LabelFrame(self.window, text="Data Export", relief=tk.RIDGE) # Defines the frame
        sav_frame.grid(row=1,column=1,sticky=tk.E + tk.W + tk.N + tk.S) # Places the frame in the grid

        # Defines variable that holds file directory
        self.sav_directory = tk.StringVar()

        # Starts file dialog to ask user for save directory
        def get_directory():
            self.sys=platform.system()
            if self.sys=='Windows':
                initdir='C:/'
            elif self.sys=='Darwin':
                initdir='/Users'
            else: initdir='/usr'
            self.sav_directory.set(filedialog.askdirectory(initialdir = initdir)) # Saves the user selected directory from dialog
            self.sav_start_button.configure(state='normal') # Start test button is enabled after directory is specified

        # Button that runs get_directory
        self.sav_directory_button = ttk.Button(sav_frame, text="Select Directory", command=get_directory)
        self.sav_directory_button.grid(row=1,column=1,sticky=tk.W,columnspan=2)

        # Read only field that displays the save directory
        sav_directory_entry = ttk.Entry(sav_frame,width=30,textvariable=self.sav_directory)
        sav_directory_entry.grid(row=2,column=1,columnspan=2,sticky=tk.W)
        sav_directory_entry.configure(state='readonly')

        # Label for the user entry field for file name
        sav_file_label = ttk.Label(sav_frame, text="File name:")
        sav_file_label.grid(row=3,column=1,sticky=tk.W)

        # User entry field for file name, default is test
        self.sav_file_entry = ttk.Entry(sav_frame,width=20)
        self.sav_file_entry.grid(row=4,column=1,columnspan=2,pady=(2,2),sticky=tk.W)
        self.sav_file_entry.insert(0,'Test')

        # Button to start test
        self.sav_start_button = ttk.Button(sav_frame,text="Start Collecting Data",command=self.beg_dat_col)
        self.sav_start_button.grid(row=5,column=1,sticky=tk.W,columnspan=2)
        self.sav_start_button.configure(state='disabled')

        # Button to stop test
        self.sav_stop_button = ttk.Button(sav_frame,text="Stop Collecting Data",command=self.stop_data)
        self.sav_stop_button.grid(row=6,column=1,sticky=tk.W,columnspan=2)
        self.sav_stop_button.configure(state='disabled')

        # Label for data collection interval (This is not exact)
        interval_label = ttk.Label (sav_frame,text="Time interval (ms):")
        interval_label.grid(row=7,column=1,sticky=tk.W)

        # Entry field for collection interval
        self.interval = ttk.Entry(sav_frame,width=10)
        self.interval.grid(row=7,column=2,sticky=tk.W)
        self.interval.insert(0,'1000')

        # - - - - -
        # Communication
        com_frame = ttk.LabelFrame(self.window,text="Communication",relief=tk.RIDGE) # Defines the frame
        com_frame.grid(row=2,column=1,sticky=tk.N+tk.E+tk.S+tk.W) # Places the frame in the grid

        com_label=ttk.Label(com_frame,text="Com Port:")
        com_label.grid(row=1,column=1,sticky=tk.W)

        def listSerialPorts():
            # A function that tries to list serial ports on most common platforms
            system_name = platform.system()
            if system_name == "Windows":
                # Scan for available ports.
                available = []
                for i in range(256):
                    try:
                        s = serial.Serial('com'+str(i+1))
                        available.append("COM"+str(i+1))
                        s.close()
                    except serial.SerialException:
                        pass
                return available
            elif system_name == "Darwin":
                # Mac
                return glob.glob('/dev/tty.usb*')# + glob.glob('/dev/cu*')
            else:
                # Assume Linux or something else
                return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')

        def refresh():
            serialports=listSerialPorts()
            self.com_select['values']=serialports
            try:
                self.com_select.current(0)
            except:
                pass
        
        self.com_select=ttk.Combobox(com_frame,postcommand=refresh)
        self.com_select.grid(row=1,column=2,sticky=tk.W)

        com_refresh=ttk.Button(com_frame,text="Refresh",command=refresh)
        com_refresh.grid(row=2,column=1,sticky=tk.W)

        # - - - - -
        # Parameters Frame
        par_frame = ttk.LabelFrame(self.window, text="Parameters", relief=tk.RIDGE)
        par_frame.grid(row=3,column=1,sticky=tk.E + tk.W + tk.N + tk.S)

        # Row labels for current settings
        IStart_label = ttk.Label(par_frame,text="Current Start (A):")
        IStart_label.grid(row=1,column=1,sticky=tk.W)

        IEnd_label = ttk.Label(par_frame,text="Current End (A):")
        IEnd_label.grid(row=2,column=1,sticky=tk.W)

        IStep_label = ttk.Label(par_frame,text="Current Step (A):")
        IStep_label.grid(row=3,column=1,sticky=tk.W)

        # Entry for setting current parameters
        self.IStart = ttk.Entry(par_frame,width=10)
        self.IStart.grid(row=1,column=2,padx=(15,15))

        self.IEnd = ttk.Entry(par_frame,width=10)
        self.IEnd.grid(row=2,column=2,padx=(15,15))

        self.IStep = ttk.Entry(par_frame,width=10)
        self.IStep.grid(row=3,column=2,padx=(15,15))

        # - - - - -
        # Plot Data Frame
        dat_frame = tk.Frame(self.window)
        dat_frame.grid(row=1,column=2,rowspan=4,sticky=tk.N + tk.E + tk.S + tk.W) # Setting rowspan to 4 so it spans the height of window
        self.window.columnconfigure(2,weight=1) # Setting Graph frame to be scalable
        self.window.rowconfigure(4,weight=1)

        # Generates figure canvas which holds matplotlib plot
        self.fig=Figure(figsize=(10,5),dpi=100)
        self.sub_fig=self.fig.add_subplot(111)
        self.sub_fig.set_xlabel('x-label')
        self.sub_fig.set_ylabel('y-label')
        self.canvas=FigureCanvasTkAgg(self.fig,dat_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=tk.YES)

    ### Starts test ###
    def beg_dat_col(self):
        # Changes buttons to normal or disabled
        self.sav_directory_button.configure(state='disabled')
        self.sav_start_button.configure(state='disabled')
        self.sav_stop_button.configure(state='normal')

        # Initialize file output with header
        self.file=str(self.sav_directory.get()) + '/' + str(self.sav_file_entry.get()) + ".csv"
        with open(self.file,'w',newline='') as fileout:
            writer=csv.writer(fileout)
            writer.writerow(['column 1','column 2','column 3']) # Define the header for the file

        # Begin figure animation
        self.start_time=time.time()
        self.ani = animation.FuncAnimation(self.fig,self.collectdata,interval=self.interval.get())
        self.canvas.show()

    ### Program for collecting and writing data ###
    def collectdata(self, i):
        
        """
        Add program to run each iteration in this function
        """

        """
        These are the functions to call the entered current values in the entry fields

        self.IStart.get()
        self.IEnd.get()
        self.IStep.get()
        """

        self.elap_time = time.time()-self.start_time # Elapsed time since test started
        self.sub_fig.clear() # Clears figure each iteration 
        labels=['label 1','label 2','label 3'] # Labels for data in graph

        # Plot data
        self.t.append(self.elap_time) # This is the x-data (time)
        if len(self.t)>self.max_graph:
            for self.y_data_arr, label in zip(self.y_data,labels):
                self.sub_fig.plot(self.t[-self.max_graph:],self.y_data_arr[-self.max_graph:],label=label)
        else:
            for self.y_data_arr, label in zip(self.y_data,labels):
                self.sub_fig.plot(self.t,self.y_data_arr,label=label)
        self.sub_fig.set_xlabel('x-label')
        self.sub_fig.set_ylabel('y-label')
        self.sub_fig.legend(loc="upper left", bbox_to_anchor=[0, 1],ncol=2, title="Legend")
    
        # Write to csv file
        str_time=[datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d, %H:%M:%S')]
        output=str_time + [self.elap_time] # This will be written to the csv file
        with open(self.file,'a',newline='') as fileout:
            writer=csv.writer(fileout)
            writer.writerow(output)

    ### Stops test ###
    def stop_data(self):
        self.sav_directory_button.configure(state='normal')
        self.sav_start_button.configure(state='normal')
        self.sav_stop_button.configure(state='disabled')
        self.sav_file_entry.delete(0,tk.END)
        self.sav_file_entry.insert(0,'Test')
        self.ani=self.ani.event_source.stop()

# Main routine to run GUI
root=tk.Tk()
program = Generic_GUI(root)
root.mainloop()

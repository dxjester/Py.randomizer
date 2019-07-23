# FILENAME: real_randomizer.py
# PROJECT: Randomizer Project
# DATE CREATED: 19-July-19
# DATE MODIFIED: 19-July-19
# VERSION: 1.0
# COMMENTS: A Python script designed 

# generate random floating point values
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import datetime

# generate random floating point values
from numpy.random import seed
from numpy.random import randint

#-------------------------- PHASE 1 -----------------------------#
#---------------------- Class Definition ------------------------#
#----------------------------------------------------------------#

# 1.1 Declare the class -----------------------------------------#
seed(6)


class int_array:
    def __init__(self):
        self.size = int(input("Enter a number: "))
        self.master_df = pd.DataFrame(index = np.arange(self.size), columns=['timesheet_date','timestamp','hours'])
        self.master_df['timesheet_date'] = datetime.datetime.now()
        self.master_df['timestamp'] = datetime.datetime.now()
        self.master_df['hours'] = np.random.randint(0,12,size=(self.size, 1))
        self.mean = 0
        self.standard_dev = 0
        self.variance = 0
    def calculate(self):
        self.master_df['timesheet_date'] = datetime.datetime.now()
        self.master_df['timestamp'] = datetime.datetime.now()
        self.mean = self.master_df['hours'].mean()
        self.standard_dev = self.master_df['hours'].std()
        self.variance = self.master_df['hours'].var()
    def hist_plot(self):
        plt.hist(self.master_df['hours'], normed=True)
    def print_array(self):
        print(self.master_df)
        print("The mean of the array is ", self.mean)
        print("The variance of the array is ", self.variance)
        print("The standard deviation of the array is ", self.standard_dev)

#-------------------------- PHASE 2 -----------------------------#
#---------------------- Script Execution ------------------------#
#----------------------------------------------------------------#

# 2.1 Script Execution Start ------------------------------------#
initial_array = int_array()
initial_array.calculate()        
initial_array.print_array()

# 2.2 Plotting --------------------------------------------------#
initial_array.hist_plot()

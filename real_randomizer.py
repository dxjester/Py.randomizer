# FILENAME: real_randomizer.py
# PROJECT: Randomizer Project
# DATE CREATED: 19-July-19
# DATE MODIFIED: 20-July-19
# VERSION: 1.0
# COMMENTS: 

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

#seed(6)

class int_array:
    def __init__(self):
        self.size = int(input("Enter a number: "))
        self.master_df = pd.DataFrame(index = np.arange(self.size), columns=['timesheet_date','timestamp','st_hours', 'ot_hours', 'dt_hours', 'total_hours'])
        self.master_df['timesheet_date'] = datetime.datetime.now()
        self.master_df['timestamp'] = datetime.datetime.now()
        self.master_df['st_hours'] = np.random.randint(0,8,size=(self.size, 1))
        self.master_df['ot_hours'] = np.random.randint(0,8,size=(self.size, 1))
        self.master_df['dt_hours'] = np.random.randint(0,8,size=(self.size, 1))
        self.mean = 0
        self.standard_dev = 0
        self.variance = 0
    def calculate(self):
        self.master_df['total_hours'] = self.master_df['st_hours'] + self.master_df['ot_hours'] + self.master_df['dt_hours']
        self.master_df['timesheet_date'] = datetime.datetime.now()
        self.master_df['timestamp'] = datetime.datetime.now()
        self.mean = self.master_df['total_hours'].mean()
        self.standard_dev = self.master_df['total_hours'].std()
        self.variance = self.master_df['total_hours'].var()
        self.variance = self.master_df['total_hours'].var()
        self.variance = self.master_df['total_hours'].var()
    def hist_plot(self):
        plt.hist(self.master_df['total_hours'])
    def print_array(self):
        print(self.master_df)
        print("The mean of of 'total_hours' is ", self.mean)
        print("The variance of the 'total_hours' is ", self.variance)
        print("The standard deviation of the 'total_hours' is ", self.standard_dev)

        
# 1.2 Declare fixed list values -----------------------------------------#
project_list = {
'project_alpha',
'project_beta',
'project_charlie', 
'project_delta',
'project_echo'}

tradecraft_list = {
'tradecraft_scaffold',
'tradecraft_insulation',
'tradecraft_abrasion', 
'tradecraft_fireproof',
'tradecraft_carpentry',
'tradecraft_roofing',
'tradecraft_construction',
'tradecraft_piping', 
'tradecraft_hvac',
'tradecraft_blasting',
'tradecraft_shoring',
'tradecraft_formwork',
'tradecraft_labor', 
'tradecraft_project_management',
'tradecraft_blasting',
}


#-------------------------- PHASE 2 -----------------------------#
#---------------------- Script Execution ------------------------#
#----------------------------------------------------------------#

# 2.1 Script Execution Start ------------------------------------#
initial_array = int_array()
initial_array.calculate()        
initial_array.print_array()

# 2.2 Plotting --------------------------------------------------#
initial_array.hist_plot()

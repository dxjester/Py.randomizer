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
<<<<<<< HEAD
# FILENAME: real_randomizer.py
# PROJECT: Randomizer Project
# DATE CREATED: 19-OCT-19
# DATE UPDATED: 26-OCT-19
# VERSION: 1.0

# import the necessary modules
import pandas as pd
import numpy as np
import matplotlib as plt
=======
import random
import datetime
>>>>>>> 447f3816da278138e3849b1899458ee742084efc

from numpy.random import seed
from numpy.random import randint

#-------------------------- PHASE 1 -----------------------------#
#---------------------- Class Definition ------------------------#
#----------------------------------------------------------------#

<<<<<<< HEAD
# ----------------- PHASE 1: CLASS & FUNCTION DECLARATION --------------------#
=======
# 1.1 Declare the class -----------------------------------------#
#seed(6)
>>>>>>> 447f3816da278138e3849b1899458ee742084efc

# 1.A: CLASS DECLARATION -----------------------------------------------------#    
class int_array:
    
    def __init__(self):
        self.size = int(input("Enter a number: "))
        self.master_df = pd.DataFrame(index = np.arange(self.size), columns=['timesheet_date','timestamp_full','st_hours', 'ot_hours', 'dt_hours', 'total_hours', 'kpi'])
        self.master_df['timesheet_date'] = datetime.datetime.today()
        self.master_df['timestamp_full'] = datetime.datetime.now()
        self.master_df['st_hours'] = np.random.randint(0,8,size=(self.size, 1))
        self.master_df['ot_hours'] = 0
        self.master_df['dt_hours'] = 0
        self.master_df['kpi'] = np.random.randint(0,20,size=(self.size, 1))
        self.mean = 0
        self.standard_dev = 0
        self.variance = 0
<<<<<<< HEAD
    
    def set_size(self):
        self.size = int(input("Enter a number: "))
        self.values = randint(0, self.size, 100)
        self.mean = self.values.mean()
        self.standard_dev = self.values.std()
        self.variance = self.values.var()

=======
        
    def calculate(self):
        self.master_df['total_hours'] = self.master_df['st_hours'] + self.master_df['ot_hours'] + self.master_df['dt_hours']
        self.mean = self.master_df['total_hours'].mean() 
        self.mean = '%.2f' % self.mean
        
        self.standard_dev = self.master_df['total_hours'].std()
        self.standard_dev = '%.2f' % self.standard_dev
        
        self.variance = self.master_df['total_hours'].var()
        self.variance = '%.2f' % self.variance
        
    def hist_plot(self):
        plt.hist(self.master_df['total_hours'])
        
>>>>>>> 447f3816da278138e3849b1899458ee742084efc
    def print_array(self):
        print(self.master_df)
        print("The mean of of 'total_hours' is ", self.mean)
        print("The variance of the 'total_hours' is ", self.variance)
        print("The standard deviation of the 'total_hours' is ", self.standard_dev)
        
<<<<<<< HEAD
# 1.A: FUNCTION DECLARATION --------------------------------------------------#    
def hist_plot(dataframe):
    plt.hist(dataframe, normed = True)


# ------------------------ PHASE 2: CODE EXECUTION ---------------------------#
=======
        print("The mean of of 'KPI' is ", self.master_df['kpi'].mean())
        print("The variance of  'KPI' is ", self.master_df['kpi'].var())
        print("The standard deviation of 'KPI' is ", self.master_df['kpi'].std())
        
        
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
>>>>>>> 447f3816da278138e3849b1899458ee742084efc
initial_array = int_array()
initial_array.calculate()        
initial_array.print_array()

<<<<<<< HEAD
hist_plot(initial_array.values)
=======
# 2.2 Plotting --------------------------------------------------#
initial_array.hist_plot()
>>>>>>> 447f3816da278138e3849b1899458ee742084efc

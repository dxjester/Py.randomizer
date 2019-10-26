# FILENAME: real_randomizer.py
# PROJECT: Randomizer Project
# DATE CREATED: 19-July-19
# DATE MODIFIED: 19-July-19
# VERSION: 1.0
# COMMENTS: A Python script designed 

# generate random floating point values
import numpy as np
import matplotlib.pyplot as plt
# FILENAME: real_randomizer.py
# PROJECT: Randomizer Project
# DATE CREATED: 19-OCT-19
# DATE UPDATED: 26-OCT-19
# VERSION: 1.0

# import the necessary modules
import pandas as pd
import numpy as np
import matplotlib as plt

from numpy.random import seed
from numpy.random import randint

seed(6)

# ----------------- PHASE 1: CLASS & FUNCTION DECLARATION --------------------#

# 1.A: CLASS DECLARATION -----------------------------------------------------#    
class int_array:
    
    def __init__(self):
        self.size = 0
        self.values = []
        self.meean = 0
        self.standard_dev = 0
        self.variance = 0
    
    def set_size(self):
        self.size = int(input("Enter a number: "))
        self.values = randint(0, self.size, 100)
        self.mean = self.values.mean()
        self.standard_dev = self.values.std()
        self.variance = self.values.var()

    def print_array(self):
        print(self.values)
        print("Array multiplied by ", self.size, " is ", self.values*self.size, "\n")
        print("The mean of the array is ", self.mean)
        print("The variance of the array is ", self.variance)
        print("The standard deviation of the array is ", self.standard_dev)
        
# 1.A: FUNCTION DECLARATION --------------------------------------------------#    
def hist_plot(dataframe):
    plt.hist(dataframe, normed = True)


# ------------------------ PHASE 2: CODE EXECUTION ---------------------------#
initial_array = int_array()
initial_array.set_size()        
initial_array.print_array()

hist_plot(initial_array.values)
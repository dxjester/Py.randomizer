# FILENAME: real_randomizer.py
# PROJECT: Randomizer Project
# DATE CREATED: 19-July-19
# DATE MODIFIED: 19-July-19
# VERSION: 1.0
# COMMENTS: A Python script designed 

# generate random floating point values
import numpy as np

# generate random floating point values
from numpy.random import seed
from numpy.random import randint

seed(6)

size = int(input("Enter a number: "))
values = randint(0, 10, size)
print(values)


print("Array multiplied by ", size, " is ", values*6)
print("The mean of the array is ", values.mean())
print("The variance of the array is ", values.var())
print("The standard deviation of the array is ", values.std())

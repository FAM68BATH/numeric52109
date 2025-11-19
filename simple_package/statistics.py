###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##

try:
    import numpy as np
    import matplotlib.pyplot as plt
except:
    print('Missing Packages: NumPy, MatplotLib')
    exit()

from simple_package import graphics

def stats_summary(A):
    if (type(A) != np.array):
        print('np.array not given. Unable to calculate summay statistics')
        exit()
    mean = np.mean(A)
    median = np.median(A)
    sd = np.std(A)
    return mean, median, sd




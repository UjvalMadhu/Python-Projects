# Project: Binary Search
# The Goal of this project is to create a function to perform a binary search on a list of numbers of any length.
# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python

# Author: Ujval Madhu
# C-Log: 26th Jan 2025
#==========================================================================================================================

import random

def binary_search(data, target):                     # Function to perform binary search on a given list of integers

    #Sorting the data first
    data.sort()

    low = 0
    high = len(data)-1

    while(1):
        
        if(data[low] == target):                      # First if checks if the value is either in low or high so as to prevent further execution
            return low
        elif (data[high] == target):
            return high
        else:
            mid = (low + high) // 2

        if(mid == low):                               # Checks if we have exhausted the list
            return -1
        elif(data[mid] < target):
            low = mid
        else:
            high = mid

n = 20                                                # Sets the total number of elements
max_val = 100                                         # Sets the range of integers
data = [random.randint(0, max_val) for i in range(n)] # Enhancing the list 
print("Data: ", data)

# Input the Target value
target = int(input("Enter target integer: "))
target_pos = binary_search(data, target)

if(target_pos == -1):
    print("Target Integer is not in List")
else:
    print(f"Target Integer is at:{target_pos}")



        
    


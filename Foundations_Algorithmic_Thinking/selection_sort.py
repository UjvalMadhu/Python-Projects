# Project: Selection Sort
# This is one of the simplest sorting algorithms, This projects aims at designing a sorting function that can accept
# a range of numbers and sort them from lowest to highest using the selection sort algorithm.

# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python

# Author: Ujval Madhu
# C-Log: 26th Jan 2025

#==========================================================================================================================

def selectionSort(sort_list):                                                     # function to perform Selection sorting on a list of numbers

    for i in range(len(sort_list) -1):                                             # Last element not required as it will be sorted
        min_i = i
        for j in range(i+1, len(sort_list)):                                       # Start from i+1 and compare upto the end of the list
            if(sort_list[min_i] > sort_list[j]):
                min_i = j
        sort_list[i], sort_list[min_i] = sort_list[min_i], sort_list[i]            # Swap with element at i the minimum value


# Code to test the sorting function

xList = [98, 25, -30, 10, 12, 24, 54, 98]
print(xList)

selectionSort(xList)
print(xList)

xList2 = [38, 27, 43, -10,  78, 77, -150]
print("Is Sorted:", end = " ")
print(all(xList2[i] <= xList2[i+1] for i in range(len(xList2)-1)))
print(xList2)
selectionSort(xList2)
print("Is Sorted:", end = " ")
print(all(xList2[i] <= xList2[i+1] for i in range(len(xList2)-1)))
print(xList2)
#==========================================================================================================
# Project: Quicksort Algorithm                                                                            |
# This is an implementation of the quicksort algorithm.                                                   |
#                                                                                                         |
# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python            |
#                                                                                                         |
# Author: Ujval Madhu                                                                                     |
# C-Log: 6th Mar 2025                                                                                     |
# All code is original and written by the Author                                                          |
# Copyright 2025 Ujval Madhu, All rights reserved                                                         |
#==========================================================================================================

import random

def quicksort_algorithm(array):

    l = len(array)
    pivot = l//2
    arr_l = []           
    arr_p = []
    arr_h = []
    sorted_array = []

    if l > 1:
    

        for i in range(0,l):
            if array[i] > array[pivot]:
                arr_h.append(array[i])
            elif array[i] < array[pivot]:
                arr_l.append(array[i])
            elif array[i] == array[pivot]:
                arr_p.append(array[i])

        
        arr_l = quicksort_algorithm(arr_l)
        arr_h = quicksort_algorithm(arr_h)

        sorted_array = arr_l + arr_p + arr_h


        return sorted_array

    else:
        return array
    
# Testing Algorithm

arr = [random.randint(0,100) for x in range(random.randint(5,10))]
print("Unsorted Array: ",arr)
arr = quicksort_algorithm(arr)
print("Sorted Array: ",arr)
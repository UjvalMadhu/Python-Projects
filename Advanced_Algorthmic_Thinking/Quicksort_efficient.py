#==========================================================================================================
#                                                                                                         |
# Project: A More Efficient Implementation of the Quicksort Algorithm                                     |
#                                                                                                         |
# This Implementation makes use of the Hoare's Algorithm for in place partitioning with a lower total     |
# average swaps for the recursive partitioning in the quicksort algorithm                                 |
#                                                                                                         |
# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python            |
#                                                                                                         |
# Author: Ujval Madhu                                                                                     |
# C-Log: 6th Mar 2025                                                                                     |
# Copyright 2025 Ujval Madhu, All rights reserved                                                         |
#                                                                                                         |
#==========================================================================================================

import random

class Sorter:
    # Haore's Partition Implelmentation
    def _h_partition(self, arr: list, lo: int, hi: int) -> int:

        #pivot = arr[(hi+lo)//2]
        pivot = arr[lo]
        i = lo
        j = hi

        while True:

            while (arr[i] < pivot and i < hi):
                i+=1
            
            while (arr[j] >= pivot and j > lo):
                j-=1
            
            if i >= j:
                return j
            # elif i == j:
            #     j-=1
            #     return j
            
            arr[i], arr[j] = arr[j], arr[i]



    # Quick Sort Main Algorithm
    def _quicksort_algorithm(self, arr: list, lo:int, hi: int) -> None:
        
        if(lo < hi):
            pivot = self._h_partition(arr, lo, hi)
            self._quicksort_algorithm(arr, lo, pivot)
            self._quicksort_algorithm(arr, pivot+1, hi)


    # Calling
    def sort(self, array: list) -> list:
        self._quicksort_algorithm(array, 0, len(array) - 1)
        return array
        
        
    
    
# Testing Algorithm
# Randomized Testing
for i in range(100):

    arr = [random.randint(0,10) for x in range(random.randint(5,10))]
    #print("Unsorted Array: ",arr)
    
    original_array = arr
    s1 = Sorter()
    print("Test id: "+str(i)+",original array:"+str(original_array))
    test_arr = sorted(arr)
    qS_array = s1.sort(arr)

    assert qS_array == test_arr, "Test id: "+str(i)+",original array:"+str(original_array)+" Array sorting error, obtained array: " + str(qS_array) +" , Required array: " + str(test_arr)

# Manual Testing

arr = [60, 27, 0, 18, 36, 75, 78]
s1 = Sorter()
test_arr = sorted(arr)
qS_array = s1.sort(arr)
print("obtained array: " + str(qS_array) +" , Required array: " + str(test_arr))
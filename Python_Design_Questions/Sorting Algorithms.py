#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///                             Sorting Algorithms                               ///
#///                                                                              ///
#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///   This Program demonstrates various sorting algorithm implementation         ///
#///   The Algorithms Include:
#///   1. Quick Sort (Fastest for random data)
#///   2. Merge Sort (For Stability)                                                                           ///
#///   3. Heap Sort  (Consistent Performance)
#///   4. Bubble Sort
#///   5. Insertion Sort (For Nearly sorted Data)
#///                                                                              ///
#///   Copyright (C) 2025 Ujval Madhu,                                            ///
#///   This program is free software: you can redistribute it and/or modify       ///
#///   it under the terms of the GNU General Public License as published by       ///
#///   the Free Software Foundation, either version 3 of the License, or          ///
#///   (at your option) any later version.                                        ///
#///                                                                              ///
#///   This program is distributed in the hope that it will be useful,            ///
#///   but WITHOUT ANY WARRANTY; without even the implied warranty of             ///
#///   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              ///
#///   GNU General Public License for more details.                               ///
#///                                                                              ///
#///   You should have received a copy of the GNU General Public License          ///
#///   along with this program.  If not, see <https://www.gnu.org/licenses/>.     ///
#///                                                                              ///
#////////////////////////////////////////////////////////////////////////////////////
#//  CVS Log
#//
#//  Id: spiral_matrix.py, v 1.0
#//
#//  $Date: 2025-3-27
#//  $Revision: 1.0 
#//  $Author:  Ujval Madhu


import random
import traceback


# 1. Quick Sort, O(nlogn)
def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) //2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# 2. Merge Sort O(nlogn)
def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):

    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Heap Sort O(nlogn)
def heap_sort(arr):
    n = len(arr)

    # Building Max Heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i , 0)

    return arr

def heapify(arr, n , i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)



array = [random.randint(1,25) for x in range(0,10)]

array1 = quick_sort(array)
array2 = merge_sort(array)
array5 = heap_sort(array)

print("Original Array :"+ str(array))

print("Quick Sorted Array: "+ str(array1))
print("Merge Sorted Array: "+ str(array2))
print("Heap Sorted Array: "+ str(array5))






































# Revision
def quick_sort2(arr):
    if(len(arr) <= 1):
        return arr
    
    pivot = len(arr) // 2

    left = [x for x in arr if x < arr[pivot]]
    mid  = [x for x in arr if x == arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]

    return quick_sort2(left) + mid + quick_sort2(right)


array3 = quick_sort2(array)
print(f"Rev quick_sort {str(array3)}")

#def merge_sort2(arr):



# array4 = merge_sort2(array)
# print(f"Rev Merge_sort {str(array4)}")

# def heap_sort2(arr):


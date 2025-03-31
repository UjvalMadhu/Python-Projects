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



array = [random.randint(1,25) for x in range(0,10)]

array1 = quick_sort(array)
array2 = merge_sort(array)

print("Original Array :"+ str(array))

print("Quick Sorted Array: "+ str(array1))
print("Merge Sorted Array: "+ str(array2))


def quick_sort2(arr):

    if len(arr)<= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]

    return quick_sort(left) +quick_sort(middle) + quick_sort(right)


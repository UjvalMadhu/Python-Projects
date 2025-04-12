#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///                           Searching Algorithms                               ///
#///                                                                              ///
#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///   This Program demonstrates various sorting algorithm implementation         ///
#///   The Algorithms Include:                                                    ///
#///   1. Linear Search                                                           ///
#///   2. Binary Search                                                           ///
#///   3. Depth First Search                                                      ///
#///   4. Breath First Search                                                     ///
#///   5. A-Star                                                                  ///
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
#//  $Date: 2025-04-11
#//  $Revision: 1.0 
#//  $Author:  Ujval Madhu

# Linear Search
def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return None

# Binary Search
def binary_search(arr, item):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left + right) // 2

        if item < mid:
            right = mid - 1
        elif item > mid:
            left = mid + 1
        else:
            return mid
    
    return None
        
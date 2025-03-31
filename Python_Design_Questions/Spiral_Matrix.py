#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///                             Spiral Matrix                                    ///
#///                                                                              ///
#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///   Given a mxn matrix, return all elements of matrix in spiral order          ///
#///   m == row, n = columns, 1 <= m,n <=10, -100 <= matrix[i][j] <= 100          ///
#///                                                                              ///
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

def spiral_matrix(matrix):

    if not matrix:
        return []
    
    m = len(matrix)
    try:
        n = len(matrix[0])
    except:
        print(matrix)
        return matrix
    
    top = 0 
    bottom = m-1
    left = 0
    right = n-1
    spiral = []
    total = m*n
    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            print(matrix[top][i],"->", end = "")
            spiral.append(matrix[top][i])
            total -=1
        top += 1

        if(total != 0):
            for j in range(top, bottom + 1):
                print(matrix[j][right],"->", end = "")
                spiral.append(matrix[j][right])
                total -=1
            right -= 1
        
        if(total != 0):
            for i in range(right, left -1, -1):
                print(matrix[bottom][i],"->", end = "")
                spiral.append(matrix[bottom][i])
                total-=1
            bottom -= 1

        if(total != 0):
            for j in range(bottom, top - 1, -1):
                print(matrix[j][left],"->", end = "")
                spiral.append(matrix[j][left])
                total -=1
            left += 1
        
        # print("\n")
        # print("top:", top, ", bottom:", bottom,", left:",left, ", right:", right)
    
    print(spiral)


mtx = [[1,2,3],[4,5,6],[7,8,9]]
mtx2 = [1]
mtx3 = [1, 2, 3]
mtx4 = [[1],[2],[3]]
mtx5 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

spiral_matrix(mtx)
spiral_matrix(mtx2)
spiral_matrix(mtx3)
spiral_matrix(mtx4)
spiral_matrix(mtx5)


    


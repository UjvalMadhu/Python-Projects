# Project: Two Sum
# Given an integer list find pairs of distinct indices in the list were the elements add up to a required sum
# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python

# Author: Ujval Madhu
# C-Log: 26th Jan 2025
#==========================================================================================================================

def two_sum(list, target):
    soln = []
    for i in range(0,len(list)):
        for j in range(len(list)):
            if(i != j):
                if (list[i] + list[j] == target):
                    soln.append((i,j))
                
    print(soln)
    return soln


assert two_sum([1, 2, 3], 4) == [(0, 2), (2,0)]
assert two_sum([1234, 5678, 9012], 14690) == [(1, 2), (2,1)]
assert two_sum([2, 2, 3], 4) == [(0, 1), (1, 0)]
assert set(two_sum([2, 2], 4)) == set([(0, 1), (1, 0)])
assert set(two_sum([8, 7, 2, 5, 3, 1], 10)) == set([(0, 2), (2, 0), (1, 4), (4, 1)])
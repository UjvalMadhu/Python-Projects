#==========================================================================================================
#                                                                                                         |
# Project: Fibonacci Function Implementation using Recursion                                              |
#                                                                                                         |                                 |                                                                                                   |
# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python            |
#                                                                                                         |
# Author: Ujval Madhu                                                                                     |
# C-Log: 6th Mar 2025                                                                                     |
# Copyright 2025 Ujval Madhu, All rights reserved                                                         |
#                                                                                                         |
#==========================================================================================================


def fibonacci_recursion(n):

    if n == 1:
        return 1
    elif n == 0:
        return 0   
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


print(fibonacci_recursion(6))
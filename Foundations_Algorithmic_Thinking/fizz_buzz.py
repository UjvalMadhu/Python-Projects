#Fizz Buzz
# This is a simple game program that counts from 1 to 100, with the following conditions:
# 1) Replaces multiples of 3 with Fizz,
# 2) Replaces multiples of 5 with Buzz, and
# 3) Replaces multiples of both 3 and 5 with FizzBuzz


# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python

# Author: Ujval Madhu
# C-Log: 26th Jan 2025

#==========================================================================================================================

for i in range (1, 101):
    if((i % 3 == 0) and (i % 5 == 0)):              # Condition check for both 3 and 5 multiples
        print("FizzBuzz", end = " ")
    elif(i % 3 == 0):                               # Condition Check for multiples of 3
        print("Fizz", end = " ")
    elif(i % 5 == 0):                               # Condition Check for multiples of 5
        print("Buzz", end = " ")
    else:                                           # Print all other Numbers
        print(i, end = " ") 
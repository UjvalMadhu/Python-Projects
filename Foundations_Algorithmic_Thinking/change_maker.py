# Project: Change Make
# The goal of this project is, when given a set of denominations of currency and a target value, to come up with combination 
# using the least amount of denomination to make the target value
# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python

# Author: Ujval Madhu
# C-Log: 26th Jan 2025
#==========================================================================================================================
 
den = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]              # US Currency Denominations 100 Dollars to 1 Cent (Penny) 

tar = float(input("Enter your amount: "))
tar = round(tar,2)                                                        # Round to avoid precision loss and also to fit denominations

sum = 0                                                                   # Stores the calculated value using denominations
comb = [0] * 12                                                           # List of 12 zeros for storing count of each denomination

for i in range(len(den)):

    while(sum < tar):
        if (sum + den[i] > tar):
            break
        sum += den[i]
        sum = round(sum, 3)
        comb[i]+=1
    
    if (round(tar - sum,2) < 0.01):
        break

print("The combination would require the following Denominations")

for i in range(len(den)):
    if(comb[i] != 0):
        print(f"{den[i]}$ :{comb[i]}")


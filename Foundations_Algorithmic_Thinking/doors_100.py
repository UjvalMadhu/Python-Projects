#100 Doors: This is a Program that is used to simulate the end result of opening 100 door with a specific pattern        
# 1. Start with 100 closed doors
# 2. Open each door until all 100 doors are open
# 3. Next, Start from the beginning and go to every 2nd door until 100, sequence would be 2, 4, 6 ...., 100
#  but if you encounter an open door close it and if you encounter a closed door open in
# 4. Then every 3rd door in the order: 3, 6, 9 .... 99
# 5. Go on in this manner until there is only a single door in a step, i.e the 100th door
# 6. Report the final result

# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python

# Author: Ujval Madhu
# C-Log: 26th Jan 2025

#==========================================================================================================================

doors = [False] * 100                         # Create 100 doors and store their states

for i in range(0, 100):                       # Iterate from 0 to 99
    for i in range(i, 100, i+1):              # Iterate as the desired sequence
        doors[i] = not doors[i]

for i in range(0, 100):                       # Print open doors
    if doors[i] is True:
        print(i+1, end = ", ")
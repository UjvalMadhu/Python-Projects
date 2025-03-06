# Project: Numbers Sort Game
# Given a set of distinct integers the user is asked to sort them in Given Time
# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python

# Author: Ujval Madhu
# C-Log: 6th Mar 2025
#==========================================================================================================================

import random, time, os, sys, threading

stop_event = threading.Event()   # Stop event to terminate threads


# Timer Thread to keep track of game time

def timer(sec):
    try:      
        for i in range(1,sec+1):
            time.sleep(1)
            
            # # print("\033[F", end="")  # for adjusting cursor but interferes with input
            # # print("\033[K", end="")

            if stop_event.is_set():
                break
        if not stop_event.is_set():
            print("Time Over")
            print("Game Stopped")

    except KeyboardInterrupt:
        print("Game Stopped")


    finally:
        stop_event.set()

# game Thread to input numbers and check correctness

def game(numbers):
    num_in = []
    i = 0
    print("Enter all numbers followed by return")
    try:
        while not stop_event.is_set():
            try:
                num = int(input())
                if num not in numbers:
                    print("Entered Number not in list try again")
                else:
                    i+=1
                    num_in.append(num)
                    if(i == len(numbers)):
                        break

                    else:
                        print("Enter Next Number")
            except:
                print("Invalid Number, Try Again")


        print("You Have Entered :", num_in)

        number = numbers.sort()
        for j in range(len(numbers)):

            if(num_in[j] != numbers[j]):
                print("Your Answer is incorrect")
                break
            elif (j == len(numbers) -1):
                print("Correct, you win")

    except KeyboardInterrupt:
        print("Game Stopped")
    finally:
        stop_event.set()



# Game Top 

def numbers_sort_game():

    num_count = random.randint(3,6)
    numbers = random.sample(range(100), num_count)
    sec = num_count*3

    print("---------- Sorting Number Game ----------- ")
    print("\nYou need to sort the given numbers within the time limit")
    input("Hit RETURN to start game and CTRL + C to Terminate\n")

    [print(i, end = "  ") for i in numbers]
    print("\n\nSort the given numbers in ",sec, "s")


    # Creating Threads
    clock_thread = threading.Thread(target = timer, args=(sec,))
    game_thread = threading.Thread(target = game, args=(numbers,))



    # Starting Thread
    clock_thread.start()
    game_thread.start()

    # Wait for thread to finish
    try:
        clock_thread.join()
        game_thread.join()
    except KeyboardInterrupt:
        print("\nGame Stopped")
    finally:
        stop_event.set()


numbers_sort_game()  # Starting the game

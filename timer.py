"""
This program is for my in-class assignment 4
timer.py is a Python script that will run the nerves of steel game
it will ask players to stand, set a random time in between 5-25 seconds and then say time is up when its done

timer.py uses the time library to help keep track of time.
timer.py uses the random library to generate a random number within the range.
"""

import time # The time library has a sleep function that will pause the script for a specified amount of time
import random # The random library allows us to generate a random number between 5-25 seconds

print("Everyone stand up") # Program to display text informing players to stand

set_time = random.randint(5, 25) # Random time between 5-25 seconds

time.sleep(set_time) # Program sleeps duration of random time chosen

print("Time is up, whoever is standing is out") # Program to display text informing players time is up

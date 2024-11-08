# risk
# author: Sylvia Chapman Kent

import numpy as np
import matplotlib.pyplot as plt

def round():

    # make dice array
    die = np.array([i for i in range(1,7)])

    # set number of rolls
    a_number_rolls=3
    d_number_rolls=2

    # roll the dice
    a_rolls=np.array([np.random.choice(die) for _ in range (a_number_rolls)])
    d_rolls=np.array([np.random.choice(die) for _ in range (d_number_rolls)])

    # sort the results in descending order
    a_rolls=np.sort(a_rolls)[::-1]
    d_rolls=np.sort(d_rolls)[::-1]

    # discard the attacker's lowest roll
    a_rolls=np.delete(a_rolls, 2)

    # compare results to determine round winner (incomplete)
'''
    if a_rolls<=d_rolls:
        print("Defence Wins!")
    else:
        print("Attack Wins!")
'''

# References:
# https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order
# https://www.geeksforgeeks.org/how-to-remove-specific-elements-from-a-numpy-array/
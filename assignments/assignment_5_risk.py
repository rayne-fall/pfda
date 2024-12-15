# risk
# author: Sylvia Chapman Kent
# simulates the game Risk

import numpy as np
import matplotlib.pyplot as plt

# number of rounds attackers and defenders have won
a_wins=0
d_wins=0

a_troops = int(input("Enter the number of attacking troops "))
d_troops = int(input("Enter the number of defending troops "))

def round():
    global a_wins
    global d_wins
    global a_troops
    global d_troops
   
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

    # decide winner of round
    outcome=a_rolls>d_rolls
    if np.all(outcome)==True:
        a_wins= a_wins+1
        d_troops= d_troops-1
    else:
        d_wins= d_wins+1
        a_troops= a_troops-1

while (a_troops >0 and d_troops >0):
    round()
'''
for _ in range (1000):
    round()
'''
# create labels for each section of plot
labels = "Attackers Win", "Defenders Win",
results = [a_wins, d_wins]

# generate pie chart with percentages labelled
plt.pie(results, autopct='%1.1f%%')

# add legend
plt.legend(labels, bbox_to_anchor=(0.75, 0, 0.5, 1))
plt.show()

# References:
# https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order
# https://www.geeksforgeeks.org/how-to-remove-specific-elements-from-a-numpy-array/
# https://stackoverflow.com/questions/74412503/cannot-access-local-variable-a-where-it-is-not-associated-with-a-value-but
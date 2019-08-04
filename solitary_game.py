import numpy as np
import pylab as plt


'''
This is a little experiment to compute the probability to win
in a popular solitary game.
'''

# first define the deck of card
deck = np.arange(1,41)

# then define the selected
ones   = [1, 11, 21, 31]
twos   = [2, 12, 22, 32]
thress = [3, 13, 23, 33]

# Now, to win the game, the selected cards (ones, twos, and threes)
# has to not be present in certain positions of the deck after a shuffle

simulations = 100000

def check_ones():
    count = 0
    for ax in ones:
        if ax in deck[0:41:3]:
            count += 1
    return count

def check_twos():
    count = 0
    for tw in twos:
        if tw in deck[1:41:3]:
            count += 1
    return count

def check_three():
    count = 0
    for th in thress:
        if th in deck[2:41:3]:
            count += 1
    return count
# first implementation with for loops

def simulation():
    simul = []
    for _ in range(simulations):
        check = 0 # check counts the number of times I lose
        np.random.shuffle(deck) # of course, a shuffle before the start
        check += check_ones()
        check += check_twos()
        check += check_three()
        simul.append(check)
    return simul

simul = simulation()

#%%

# at this point I have the number of times I lose
# and the number of times I win. And also the number of times I would
# have lose in every single game

losses = np.count_nonzero(simul)

print(losses)

loss_probability = losses / simulations
win_probability  = 1. - loss_probability

print('Win probability  : {:.5f}'.format(win_probability))
print('Loss probability : {:.5f}'.format(loss_probability))

# Now I have computed the probabilities to win and to lose
# but I want also the distribution of the losses, So how many
# time i loss in a game on average

plt.hist(simul)

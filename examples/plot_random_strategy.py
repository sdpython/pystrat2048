"""
Tries a random strategy and show the results
============================================

The following examples runs the game 2048 and keeps
the highest number obtained for every try and two strategies.
"""
import numpy
import matplotlib.pyplot as plt

from pystrat2048.random_strategy import (
    random_strategy, random_strategy_all_but_one
)
from pystrat2048 import evaluate_strategy

##############################
# The first strategy :func:`random_strategy
# <pystrat2048.random_strategy.random_strategy>`
# draws a random direction.

gen1 = evaluate_strategy(random_strategy, 50)
res1 = list(gen1)
res1.sort()
print(res1)

##############################
# The second strategy :func:`random_strategy_all_but_one
# <pystrat2048.random_strategy.random_strategy_all_but_one>`
# draws a random direction among four except one.

gen2 = evaluate_strategy(random_strategy_all_but_one, 50)
res2 = list(gen2)
res2.sort()
print(res2)

#########################################
# Finaly plots the gains obtained by the two strategies.

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.bar(numpy.arange(len(res1)), res1, color="b",
       label="random", width=0.4)
ax.bar(numpy.arange(len(res2)) + 0.4, res2, color="orange",
       label="all_but_one", width=0.4)
ax.set_title("Compares two strategies for 2048.")
ax.legend()

###########################
# One seems better but 50 tries
# does not seem to be enough to be fully sure.
plt.show()

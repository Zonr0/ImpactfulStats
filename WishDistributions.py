## First, lets import the libraries we will need:

import numpy as np
import matplotlib.pyplot as plt
import math
import banners
from scipy import stats


def roll_probability(n):
    """Returns the cumulative(?) probability of pulling a 5 star"""
    p_normal = 0.006
    p_pity = 0.33
    non_five_star_chance = 1 - p_normal
    non_five_star_chance_pity = 1 - p_pity
    base_probability = math.pow(non_five_star_chance, min(n, 75))
    if n <= 75:
        return 1 - base_probability
    # elif n == 90:
    #     return 1 -
    else:
        # Need to fix this. Plateus at 75. Probably some kind of double counting?
        return 1 - base_probability * (math.pow(non_five_star_chance_pity, n - 75))

def individual_probability(n):
    p = 0.006
    q = 0.33
    if n <= 75:
        return -math.pow((1 - p),n) * math.log(1-p)
    else:
        return -math.pow((1 - p),75) * math.pow(1 - q,n-75) * math.log(1-q)

def test_distributions():
    vroll = np.vectorize(roll_probability)
    vind = np.vectorize(individual_probability)

    num_rolls = 90
    probability = 0.06

    fig, axs = plt.subplots(1,1)
    ax1 = axs

    rolls = np.arange(1, num_rolls + 1)
    ax1.bar(rolls, vind(rolls))

    plt.show()


if __name__ == '__main__':
    test_distributions()
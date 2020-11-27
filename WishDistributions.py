## First, lets import the libraries we will need:

import numpy as np
import matplotlib.pyplot as plt
import math
import banners
from scipy import stats


def roll_probability(n):
    base_probability = 1 - math.pow(1 - 0.006, min(n,54))
    if n <= 75:
        return base_probability
    # elif n == 90:
    #     return 1 -
    else:
        # Need to fix this. Plateus at 75. Probably some kind of double counting?
        return base_probability * (1 - math.pow(1 - 0.33, n - 75))


def test_distributions():
    vroll = np.vectorize(roll_probability)

    num_rolls = 90
    probability = 0.06

    fig, axs = plt.subplots(1,1)
    ax1 = axs

    rolls = np.arange(1, num_rolls + 1)
    ax1.bar(rolls, vroll(rolls))

    plt.show()


if __name__ == '__main__':
    test_distributions()
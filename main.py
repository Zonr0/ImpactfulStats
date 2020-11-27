import numpy as np
import matplotlib.pyplot as plt
import banners
from constants import *
from scipy import stats



#%% Model parameters

n=1 # Number successes
p_cons = banners.DEFAULT_EVENT_RATES.fiveStarCons #* banners.DEFAULT_EVENT_RATES.fiveStarPriorityRate# Probability of success


primo_spend = 181
usd_spend = 200
num_pulls = 0 # Existing wish items

primo_spend += usd_spend * PRIMO_PER_USD_BEST
num_pulls += primo_spend // WISH_PRIMO_COST

print(f"Probability assuming a total of {num_pulls} pulls.")

## Simple Model
simple_model = stats.binom(n=num_pulls,p=p_cons)

## Complex (Speculative) Model

class genshin_speculative(stats.rv_discrete):
    """Speculative model for the rates of Genshin Impact. Based on formula reverse engineered by the
     Chinese playerbase. Models a soft pity system that kicks in at a given point."""
    def __init__(self,base,soft_threshold,soft_increase,hard_threshold):
        xk = np.arange(hard_threshold + 1)
        # Error: probabilities of pk must sum to 1.
        f = np.vectorize(lambda x: base + soft_increase if x > soft_threshold else (1 if x == hard_threshold else base))
        pk = f(xk)
        super().__init__(values=(xk, pk))


complex_model = genshin_speculative(banners.DEFAULT_EVENT_RATES.fiveStarCons,
                                    banners.DEFAULT_EVENT_RATES.fiveStarPityRampThresh,
                                    banners.DEFAULT_EVENT_RATES.fiveStarSoftPityRate,
                                    banners.DEFAULT_EVENT_RATES.fiveStarPity)

#%% Expected number of copies of limited 5 star character.
mean_rolls_per_char = stats.nbinom.mean(n=n, p=p)
print(f"On average, you would need {mean_rolls_per_char} pulls to get {n} copies of the limited character.")
print(f"This is equal to {mean_rolls_per_char * WISH_PRIMO_COST} gems or ${(mean_rolls_per_char * WISH_PRIMO_COST) / PRIMO_PER_USD_BEST:.2f}")
successes = np.arange(0, 11)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
ax1 = axs[0]
ax2 = axs[1]
distribution = complex_model
print(distribution.cdf(1))
ax1.bar(successes, 100 * distribution.pmf(successes))
ax2.bar(successes, 100 * (1 - distribution.cdf(successes - 1)))
# ppf takes a percentile and returns the value at that percentile
# ax2.plot(successes,stats.binom.ppf(q=successes, n=num_pulls, p=p))

# Format the plot
start, end = ax1.get_xlim()
ax1.set_xlabel(xlabel="Copies of 5 Star Limited Character")
ax1.xaxis.set_ticks(successes)

ax1.set_ylim(0, 100)
ax2.set_ylim(0, 100)
ax1.set_ylabel(ylabel="Exactly this many")
ax2.set_ylabel(ylabel="At least this many")
plt.show()


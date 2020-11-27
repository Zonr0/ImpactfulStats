import copy

class GachaRates:
    def __init__(self):
        # Values are defaults
        self.fiveStarRaw = 0.006
        self.fiveStarCons = 0.016
        self.fiveStarChar = 0.003
        self.fiveStarWeap = 0.003
        self.fiveStarPity = 90
        self.fiveStarPityRampThresh = 75 # When soft pity kicks in
        self.fiveStarSoftPityRate = 0.324
        self.fiveStarPriorityRate = 0.5
        self.fourStarRaw = 0.051
        self.fourStarChar = 0.0255
        self.fourStarWeap = 0.0255
        self.fourStarCons = 0.13
        self.fourStarPity = 10
        self.fourStarPityRampThresh = 8
        self.fourStarSoftPityRate = 0.511
        self.fourStarPriorityRate = 0.5


DEFAULT_STANDARD_RATES = GachaRates()
DEFAULT_EVENT_RATES = GachaRates()
DEFAULT_EVENT_RATES.fiveStarChar = 0.006
DEFAULT_EVENT_RATES.fiveStarWeap = 0.00

class Banner:
    def __init__(self,rates=DEFAULT_STANDARD_RATES):
        self.rates = copy.deepcopy(DEFAULT_STANDARD_RATES)
        self.priorityFiveStars = 0
        self.priorityFourStars = 0


STANDARD_WISH = Banner()
STANDARD_EVENT = Banner(rates=DEFAULT_EVENT_RATES)
STANDARD_EVENT.priorityFiveStars = 1
STANDARD_EVENT.priorityFourStars = 3

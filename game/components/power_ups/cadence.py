from game.utils.constants import CADENCE, CADENCE_TYPE
from game.components.power_ups.power_up import PowerUp

class Cadence(PowerUp):
    def __init__(self):
        self.image = CADENCE
        super().__init__(self.image)
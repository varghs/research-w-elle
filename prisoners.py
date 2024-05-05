import dilemma
import numpy as np


"""
Always cheats.
"""
class Cheater(dilemma.Prisoner):
    def choose(self, matrix: dilemma.PayoffMatrix, num: int) -> dilemma.Choice:
        return dilemma.Choice.CHEAT


"""
Always cooperates.
"""
class Cooperator(dilemma.Prisoner):
    def choose(self, matrix: dilemma.PayoffMatrix, num: int) -> dilemma.Choice:
        return dilemma.Choice.COOPERATE

 

"""
Picks the outcome with the highest potential payoff.
"""
class Greedy(dilemma.Prisoner):
    def choose(self, matrix: dilemma.PayoffMatrix, num: int) -> dilemma.Choice:
        max_idx = np.unravel_index(
            np.argmax(matrix.payoffs[:, :, num]),
            matrix.payoffs[:, :, num].shape
            )
        return max_idx[num]
    
"""
Picks the outcome with the highest potential payoff for their opponent.
"""
class Altruist(dilemma.Prisoner):
    def choose(self, matrix: dilemma.PayoffMatrix, num: int) -> dilemma.Choice:
        other_num = (num + 1) % 2
        max_idx = np.unravel_index(
            np.argmax(matrix.payoffs[:, :, other_num]),
            matrix.payoffs[:, :, other_num].shape
            )
        return max_idx[num]
    

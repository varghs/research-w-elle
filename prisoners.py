import dilemma
import numpy as np


class Cheater(dilemma.Prisoner):
    """
    Always cheats.
    """

    def choose(self, matrix: dilemma.PayoffMatrix, num: int) -> dilemma.Choice:
        return dilemma.Choice.CHEAT


class Cooperator(dilemma.Prisoner):
    """
    Always cooperates.
    """

    def choose(self, matrix: dilemma.PayoffMatrix, num: int) -> dilemma.Choice:
        return dilemma.Choice.COOPERATE


class Greedy(dilemma.Prisoner):
    """
    Picks the outcome with the highest potential payoff.
    """

    def choose(self, matrix: dilemma.PayoffMatrix, num: int) -> dilemma.Choice:
        max_idx = np.unravel_index(
            np.argmax(matrix.payoffs[:, :, num]), matrix.payoffs[:, :, num].shape
        )
        return max_idx[num]


class Altruist(dilemma.Prisoner):
    """
    Picks the outcome with the highest potential payoff for their opponent.
    """

    def choose(self, matrix: dilemma.PayoffMatrix, num: int) -> dilemma.Choice:
        other_num = (num + 1) % 2
        max_idx = np.unravel_index(
            np.argmax(matrix.payoffs[:, :, other_num]),
            matrix.payoffs[:, :, other_num].shape,
        )
        return max_idx[num]

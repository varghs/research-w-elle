import dilemma
import numpy as np
import random
from collections import defaultdict


class Cheater(dilemma.Prisoner):
    """
    Always cheats.
    """

    def choose(
        self, matrix: dilemma.PayoffMatrix, num: int, other_player: str
    ) -> dilemma.Choice:
        return dilemma.Choice.CHEAT


class Cooperator(dilemma.Prisoner):
    """
    Always cooperates.
    """

    def choose(
        self, matrix: dilemma.PayoffMatrix, num: int, other_player: str
    ) -> dilemma.Choice:
        return dilemma.Choice.COOPERATE


class Greedy(dilemma.Prisoner):
    """
    Picks the outcome with the highest potential payoff.
    """

    def choose(
        self, matrix: dilemma.PayoffMatrix, num: int, other_player: str
    ) -> dilemma.Choice:
        max_idx = np.unravel_index(
            np.argmax(matrix.payoffs[:, :, num]), matrix.payoffs[:, :, num].shape
        )
        return max_idx[num]


class Altruist(dilemma.Prisoner):
    """
    Picks the outcome with the highest potential payoff for their opponent.
    """

    def choose(
        self, matrix: dilemma.PayoffMatrix, num: int, other_player: str
    ) -> dilemma.Choice:
        other_num = (num + 1) % 2
        max_idx = np.unravel_index(
            np.argmax(matrix.payoffs[:, :, other_num]),
            matrix.payoffs[:, :, other_num].shape,
        )
        return max_idx[num]


class Random(dilemma.Prisoner):
    """
    Picks a random choice
    """

    def choose(
        self, matrix: dilemma.PayoffMatrix, num: int, other_player: str
    ) -> dilemma.Choice:
        return random.choice(list(dilemma.Choice))


class TitForTat(dilemma.Prisoner):
    """
    Does whatever the other player did on their last turn.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.previous_choices = {}

    def choose(
        self, matrix: dilemma.PayoffMatrix, num: int, other_player: str
    ) -> dilemma.Choice:
        if other_player not in self.previous_choices:
            return dilemma.Choice.COOPERATE
        return self.previous_choices[other_player]

    def update_strat(self, other_player: str, other_player_choice: dilemma.Choice):
        self.previous_choices[other_player]

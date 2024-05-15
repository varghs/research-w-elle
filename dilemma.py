from enum import IntEnum
from abc import ABC, abstractmethod
from typing import Tuple, Type
import numpy as np


class Choice(IntEnum):
    COOPERATE = 0
    CHEAT = 1


class PayoffMatrix:
    def __init__(
        self, cooperate_payoff, cheat_win_payoff, cheat_lose_payoff, cheat_both_payoff
    ):
        self.cooperate_payoff = cooperate_payoff
        self.cheat_win_payoff = cheat_win_payoff
        self.cheat_lose_payoff = cheat_lose_payoff
        self.cheat_both_payoff = cheat_both_payoff
        self.payoffs = np.array(
            [
                [
                    (cooperate_payoff, cooperate_payoff),
                    (cheat_lose_payoff, cheat_win_payoff),
                ],
                [
                    (cheat_win_payoff, cheat_lose_payoff),
                    (cheat_both_payoff, cheat_both_payoff),
                ],
            ]
        )

    def get_payoffs(self, choice1: Choice, choice2: Choice):
        return self.payoffs[choice1, choice2]

    def update(self, choice1: Choice, choice2: Choice):
        if choice1 == Choice.CHEAT and choice2 == Choice.COOPERATE:
            self.cheat_win_payoff -= 0.5
            self.payoffs[choice1, choice2] = (
                self.cheat_win_payoff,
                self.cheat_lose_payoff,
            )
            self.payoffs[choice2, choice1] = (
                self.cheat_lose_payoff,
                self.cheat_win_payoff,
            )

        if choice1 == Choice.COOPERATE and choice2 == Choice.CHEAT:
            self.cheat_win_payoff -= 0.5
            self.payoffs[choice1, choice2] = (
                self.cheat_lose_payoff,
                self.cheat_win_payoff,
            )
            self.payoffs[choice2, choice1] = (
                self.cheat_win_payoff,
                self.cheat_lose_payoff,
            )

        if choice1 == Choice.CHEAT and choice2 == Choice.CHEAT:
            self.cheat_both_payoff -= 0.25
            self.payoffs[choice1, choice2] = (
                self.cheat_both_payoff,
                self.cheat_both_payoff,
            )

        if choice1 == Choice.COOPERATE and choice2 == Choice.COOPERATE:
            self.cooperate_payoff += 0.75
            self.payoffs[choice1, choice2] = (
                self.cooperate_payoff,
                self.cooperate_payoff,
            )


class Prisoner(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def choose(self, matrix: PayoffMatrix, num: int, other_player: str) -> Choice:
        pass

    @abstractmethod
    def update_strat(self, other_player: str, other_player_choice: Choice):
        pass


class PrisonersDilemma:
    def __init__(
        self, matrix: PayoffMatrix, agent1: Type[Prisoner], agent2: Type[Prisoner]
    ):
        self.matrix = matrix
        self.agent1 = agent1
        self.agent2 = agent2

    def play(self):
        """Plays one iteration of the game."""
        choice1 = self.agent1.choose(self.matrix, 0)
        choice2 = self.agent2.choose(self.matrix, 1)
        return (self.matrix.get_payoffs(choice1, choice2), choice1, choice2)

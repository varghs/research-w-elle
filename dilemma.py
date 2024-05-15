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


class Prisoner(ABC):
    @abstractmethod
    def choose(self, matrix: PayoffMatrix, num: int) -> Choice:
        pass


class PrisonersDilemma:
    def __init__(
        self, matrix: PayoffMatrix, agent1: Type[Prisoner], agent2: Type[Prisoner]
    ):
        self.matrix = matrix
        self.agent1 = agent1
        self.agent2 = agent2

    def play(self) -> Tuple[Type[Choice]]:
        """Plays one iteration of the game.

        Returns:
            Tuple[Type[Choice]]: (payoff1, payoff2)
        """
        choice1 = self.agent1.choose(self.matrix, 0)
        choice2 = self.agent2.choose(self.matrix, 1)
        return self.matrix.get_payoffs(choice1, choice2)

from typing import List, Type, Dict
from dilemma import Prisoner, PayoffMatrix, PrisonersDilemma
from collections import defaultdict
from copy import copy


class Results:
    def __init__(self, outcomes):
        self.game_list = outcomes

    def calculate_scores(self) -> Dict:
        wins = defaultdict(int)
        for game in self.game_list:
            wins[game.player1] += game.outcomes[0]
            wins[game.player2] += game.outcomes[1]

        return wins

    def pairing_outputs(self) -> Dict:
        outputs = {}
        for game in self.game_list:
            if not ((game.player1, game.player2) in outputs):
                outputs[(game.player1, game.player2)] = [0, 0]
            outputs[(game.player1, game.player2)] = [
                x + y
                for x, y in zip(outputs[(game.player1, game.player2)], game.outcomes)
            ]

        return outputs


class Result:
    def __init__(self, player1: str, player2: str, outcomes: List[int]):
        self.player1 = player1
        self.player2 = player2
        self.outcomes = outcomes

    def __str__(self) -> str:
        return f"{self.player1}, {self.player2}, {self.outcomes}"


class Tournament:
    def __init__(self, players: List[Type[Prisoner]]) -> None:
        self.players = players
        self.num_players = len(players)
        self.matrices = [
            PayoffMatrix(7, 10, 2, 3)
            for i in range(self.num_players * (self.num_players - 1) // 2)
        ]

    def play(self, num_rounds: int) -> Results:
        games = []
        for rounds in range(num_rounds):
            for i in range(self.num_players):
                for j in range(i + 1, self.num_players):
                    game = PrisonersDilemma(
                        self.matrices[
                            i * (self.num_players - 1) + j - 1 - (i * (i + 1) // 2)
                        ],
                        self.players[i],
                        self.players[j],
                    )
                    outcome, choice1, choice2 = game.play()
                    result = Result(
                        self.players[i].name, self.players[j].name, copy(outcome)
                    )
                    games.append(result)
                    self.matrices[
                        i * (self.num_players - 1) + j - 1 - (i * (i + 1) // 2)
                    ].update(choice1, choice2)
                    self.players[i].update_strat(self.players[j].name, choice2)
                    self.players[j].update_strat(self.players[i].name, choice1)

        return Results(games)

from typing import List, Type
from dilemma import Prisoner

class Results:
    def __init__(self, outcomes):
        self.game_list = outcomes
    
    def calculate_wins(self) -> :
        
        

class Tournament:
    def __init__(self, players: List[Type[Prisoner]]) -> None:
        self.players = players
        
    def play(self) -> Results:
        games = []
        
import prisoners
import tournament

cheater1 = prisoners.Cheater("cheater1")
cooperator1 = prisoners.Cooperator("cooperator1")
greedy1 = prisoners.Greedy("greedy1")
altruist1 = prisoners.Altruist("altruist1")
random1 = prisoners.Random("random1")
titfortat1 = prisoners.TitForTat("titForTat1")
prisoners_list = [cheater1, cooperator1, greedy1, altruist1, random1, titfortat1]

tourney = tournament.Tournament(prisoners_list)
results = tourney.play(100)
print(results.calculate_scores())

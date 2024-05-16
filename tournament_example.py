import prisoners
import tournament

cheater1 = prisoners.Cheater("cheater1")
cooperator1 = prisoners.Cooperator("cooperator1")
greedy1 = prisoners.Greedy("greedy1")
altruist1 = prisoners.Altruist("altruist1")
random1 = prisoners.Random("random1")
titfortat1 = prisoners.TitForTat("titForTat1")
cheater2 = prisoners.Cheater("cheater2")
cooperator2 = prisoners.Cooperator("cooperator2")
greedy2 = prisoners.Greedy("greedy2")
altruist2 = prisoners.Altruist("altruist2")
random2 = prisoners.Random("random2")
titfortat2 = prisoners.TitForTat("titForTat2")
prisoners_list = [
    cheater1,
    cooperator1,
    greedy1,
    altruist1,
    random1,
    titfortat1,
    cheater2,
    cooperator2,
    greedy2,
    altruist2,
    random2,
    titfortat2,
]

tourney = tournament.Tournament(prisoners_list)
results = tourney.play(100)
print(results.calculate_scores())

import prisoners
import tournament
from collections import defaultdict
import re

# cheater1 = prisoners.Cheater("cheater1")
# cooperator1 = prisoners.Cooperator("cooperator1")
# random1 = prisoners.Random("random1")
# titfortat1 = prisoners.TitForTat("titForTat1")
# cheater2 = prisoners.Cheater("cheater2")
# cooperator2 = prisoners.Cooperator("cooperator2")
# random2 = prisoners.Random("random2")
# titfortat2 = prisoners.TitForTat("titForTat2")
# cheater3 = prisoners.Cheater("cheater3")
# cooperator3 = prisoners.Cooperator("cooperator3")
# random3 = prisoners.Random("random3")
# titfortat3 = prisoners.TitForTat("titForTat3")
# cheater4 = prisoners.Cheater("cheater4")
# cooperator4 = prisoners.Cooperator("cooperator4")
# random4 = prisoners.Random("random4")
# titfortat4 = prisoners.TitForTat("titForTat4")
# cheater5 = prisoners.Cheater("cheater5")
# cooperator5 = prisoners.Cooperator("cooperator5")
# random5 = prisoners.Random("random5")
# titfortat5 = prisoners.TitForTat("titForTat5")
# cheater6 = prisoners.Cheater("cheater6")
# cooperator6 = prisoners.Cooperator("cooperator6")
# random6 = prisoners.Random("random6")
# titfortat6 = prisoners.TitForTat("titForTat6")
# cheater7 = prisoners.Cheater("cheater7")
# cooperator7 = prisoners.Cooperator("cooperator7")
# random7 = prisoners.Random("random7")
# titfortat7 = prisoners.TitForTat("titForTat7")
# cheater8 = prisoners.Cheater("cheater8")
# cooperator8 = prisoners.Cooperator("cooperator8")
# random8 = prisoners.Random("random8")
# titfortat8 = prisoners.TitForTat("titForTat8")
# cheater9 = prisoners.Cheater("cheater9")
# cooperator9 = prisoners.Cooperator("cooperator9")
# random9 = prisoners.Random("random9")
# titfortat9 = prisoners.TitForTat("titForTat9")
# cheater10 = prisoners.Cheater("cheater10")
# cooperator10 = prisoners.Cooperator("cooperator10")
# random10 = prisoners.Random("random10")
# titfortat10 = prisoners.TitForTat("titForTat10")

# prisoners_list = [
#     cheater1,
#     cooperator1,
#     random1,
#     titfortat1,
#     cheater2,
#     cooperator2,
#     random2,
#     titfortat2,
#     cheater3,
#     cooperator3,
#     random3,
#     titfortat3,
#     cheater4,
#     cooperator4,
#     random4,
#     titfortat4,
#     cheater5,
#     cooperator5,
#     random5,
#     titfortat5,
#     cheater6,
#     cooperator6,
#     random6,
#     titfortat6,
#     cheater7,
#     cooperator7,
#     random7,
#     titfortat7,
#     cheater8,
#     cooperator8,
#     random8,
#     titfortat8,
#     cheater9,
#     cooperator9,
#     random9,
#     titfortat9,
#     cheater10,
#     cooperator10,
#     random10,
#     titfortat10,
# ]


def strip_numbers(string):
    return re.sub(r"\d+", "", string)


# tourney = tournament.Tournament(prisoners_list)
# results = tourney.play(100)
# scores = results.calculate_scores()
# scores_summed = defaultdict(int)
# for player in scores:
#     scores_summed[strip_numbers(player)] += scores[player]

# print(scores_summed)

for i in range(2, 9):
    num_players = 2**i
    num_of_each = num_players // 4
    prisoners_list = []
    for i in range(num_of_each):
        prisoners_list.append(prisoners.Cheater(f"cheater{i}"))
        prisoners_list.append(prisoners.Cooperator(f"cooperator{i}"))
        prisoners_list.append(prisoners.Random(f"random{i}"))
        prisoners_list.append(prisoners.TitForTat(f"titForTat{i}"))
    tourney = tournament.Tournament(prisoners_list)
    results = tourney.play(100)
    scores = results.calculate_scores()
    scores_summed = defaultdict(int)
    for player in scores:
        scores_summed[strip_numbers(player)] += scores[player]
    print(scores_summed)


for i in range(2, 10):
    num_players = 2**i
    num_of_each = num_players // 4
    prisoners_list = [
        prisoners.Cheater("cheater1"),
        prisoners.Cooperator("cooperator1"),
        prisoners.Random("random1"),
    ]
    for i in range(num_of_each):
        prisoners_list.append(prisoners.TitForTat(f"titForTat{i}"))
    tourney = tournament.Tournament(prisoners_list)
    results = tourney.play(100)
    scores = results.calculate_scores()
    scores_summed = defaultdict(int)
    for player in scores:
        scores_summed[strip_numbers(player)] += scores[player]
    scores_summed["titForTat"] /= num_of_each
    print(scores_summed)

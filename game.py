import dilemma, prisoners

matrix = dilemma.PayoffMatrix(3, 5, 0, 1)
greedy1 = prisoners.Greedy("greedy1")
titfortat1 = prisoners.TitForTat("titForTat1")
game = dilemma.PrisonersDilemma(matrix, greedy1, titfortat1)

outcome, choice1, choice2 = game.play()
titfortat1.update_strat(greedy1.name, choice1)
print(outcome, choice1, choice2)

print(game.play())

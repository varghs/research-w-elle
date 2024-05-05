import dilemma, prisoners

matrix = dilemma.PayoffMatrix(3, 5, 0, 1)
greedy1 = prisoners.Greedy()
greedy2 = prisoners.Greedy()
game = dilemma.PrisonersDilemma(matrix, greedy1, greedy2)

print(game.play())
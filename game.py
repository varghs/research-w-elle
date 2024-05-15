import dilemma, prisoners

matrix = dilemma.PayoffMatrix(3, 5, 0, 1)
greedy1 = prisoners.Greedy("greedy1")
random1 = prisoners.Random("random1")
game = dilemma.PrisonersDilemma(matrix, greedy1, random1)

print(game.play())

# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

maxArray = []
maxValFirst = 0
maxValSecond = 0
maxValThird = 0
maxValLast = 0

for firstVal in range(len(tab[0])):
    if tab[0][firstVal] > maxValFirst:
        maxValFirst = tab[0][firstVal]
print(maxValFirst)
maxArray.append(maxValFirst)

for secondVal in range(len(tab[1])):
    if tab[1][secondVal] > maxValSecond:
        maxValSecond = tab[1][secondVal]
print(maxValSecond)
maxArray.append(maxValSecond)

for thirdVal in range(len(tab[2])):
    if tab[2][thirdVal] > maxValThird:
        maxValThird = tab[2][thirdVal]
print(maxValThird)
maxArray.append(maxValThird)

for maxVal in range(len(maxArray)):
    if maxArray[maxVal] > maxValLast:
        maxValLast = maxArray[maxVal]

print("La valeur maximum est : ", maxValLast," et elle se trouve à l'indice ", tab[2].index(maxValLast))


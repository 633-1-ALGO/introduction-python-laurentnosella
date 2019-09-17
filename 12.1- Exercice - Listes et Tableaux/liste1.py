# Problème : Réaliser une table de multiplication de taile 10x10 en utilisant la liste fournie.
# Résultat attendu : un affichage comme ceci :   1  2  3  4  5  6  7  8  9  10
#                                             1  1  2  3  4  5  6  7  8  9  10
#                                             2  2  4  6  8  10 12 14 16 18 20
#                                             . .  .  .  .  .  .  .  .  .  .
# Indication :   L'alignement rectiligne n'est pas une contrainte, tant que la table est visible ligne par ligne c'est ok.
#               Si vous êtes perfectionnistes faites vous plaisir.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arrayTemp = liste

for i in range(1,10):
    print(arrayTemp)
    arrayTemp = []
    for num in range(0,len(liste)):
        #print(liste[num]*i)
        arrayTemp.append(liste[num]*i)
        #arrayTemp[num] = liste[num]*i

print(arrayTemp)



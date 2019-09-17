# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

for i in range(0,len(B)):
    for num in range(0,len(B)-1):
        if B[i] < B[num]:
            stockGrand = B[num]
            stockPetit = B[i]
            B[i] = stockGrand
            B[num] = stockPetit

print(B)


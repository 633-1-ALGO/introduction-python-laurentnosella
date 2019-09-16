# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]

total = 0
cpt = 0
for element in A:
    total = total + element
    #print("indice courant = ", cpt)
    #print("element courant = ", element)
    #print("-------------------")
    cpt = cpt + 1
print("")
print("Moyenne du tableau : ", total/cpt)

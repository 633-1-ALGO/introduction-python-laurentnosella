# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

print("le mot 'Exemple' est présent ", texte.count("exemple"), " fois")
print()
print(texte.replace("est","représente"))
txt = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."[::-1]
print("Bonus : " + txt)

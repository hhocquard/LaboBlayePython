# approximationDePI
# Ce script calcule une approximation de PI
# lecture données
nbEtapes = int(input("Entrer le nombre d'étapes : "))
# initialisations
approxPi = 1
signe = -1
# boucle de calcul
for i in range (1,nbEtapes+1):
    # on ajoute le i-ième terme
    approxPi = approxPi + signe / (2*i+1)
    # on change de signe pour le tour suivant
    signe = -signe
# affichage du résultat
approxPi = 4 * approxPi
print (approxPi)







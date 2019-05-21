# factorielle
# Ce script permet de calculer la factorielle d’un entier naturel 
# entré au clavier
# lecture des données
n = int(input("n ? "))
# initialisation
fact = 1
# boucle de calcul
for i in range(2,n+1):
    fact = fact * i
# affichage du résultat
print("La factorielle de",n,"vaut",fact)














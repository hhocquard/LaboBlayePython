# intersectionIntervalles
# Ce script permet de calculer l’intersection de deux intervalles
# d’entiers de la forme [a, b] et [c, d].
# lecture données
a = float(input("Entrer a : "))
b = float(input("Entrer b : "))
c = float(input("Entrer c : "))
d = float(input("Entrer d : "))
# calcul du maximum des bornes inférieures
if (a < c):
    max = c
else:
    max = a
# calcul du minimum des bornes supérieures
if (b < d):
    min = b
else:
    min = d
# affichage du résultat
if (max <= min):
    print ("[", max,";",min,"]")
else:
    print ("Intersection vide.")






# longueurSegment
# Ce script calcule la longueur d’un segment AB 
# (XA, YA, XB, YB donnés)
import math
# lecture données
XA = float(input("XA : "))
YA = float(input("YA : "))
XB = float(input("XB : "))
YB = float(input("YB : "))
# calcul de la longueur
longueur = math.sqrt ( ((XB-XA) * (XB-XA)) + ((YB-YA) * (YB-YA)) )
# affichage résultat
print("longueur du segment : ", longueur)


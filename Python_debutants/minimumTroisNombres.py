# minimumTroisNombres
# Ce script permet d’afficher le plus petit de trois nombres 
# entrés au clavier.
# lecture données
a = int(input("a ? "))
b = int(input("b ? "))
c = int(input("c ? "))
# comparaisons
if (a < b):
    if (a < c):
        min = a
    else:
        min = c
elif (b < c):
    min = b
else:
    min = c
# Affichage minimum
print("Le plus petit de ces trois entiers est",min)















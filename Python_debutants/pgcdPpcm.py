# pgcdPpcm
# ce script permet de calculer le PGCD et le PPCM de deux entiers
# naturels non nuls entrés au clavier
# lecture des données
a = int(input("a ? "))
b = int(input("b ? "))
# initialisations
aa = a
bb = b
reste = a % b
# boucle de calcul
while (reste != 0):
    aa = bb
    bb = reste
    reste = aa % bb
# calcul du pgcd et du ppcm
pgcd = bb
ppcm = ( a * b ) // pgcd
# affichage résultat
print("PGCD :",pgcd,"PPCM :",ppcm)









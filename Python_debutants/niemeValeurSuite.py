# niemeValeurSuite
# ce script permet de calculer la n-ième valeur d’une suite de la
# forme un = aun-1 + b, u0 = c
# lecture des données
a = int(input("a ? "))
b = int(input("b ? "))
c = int(input("c ? "))
n = int(input("n ? "))
# initialisations
un = c
# boucle de calcul
for i in range(1,n+1):
    un = a * un + b
# affichage résultat
print("la",n,"ième valeur de la suite est",un)



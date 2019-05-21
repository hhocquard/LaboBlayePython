# fibonacci
# Ce script permet de calculer le nombre de Fibonacci F(n)
# lecture des données
n = int(input("n ? "))
# initialisations
fibo = 1
fiboprecedent = 0
# test si cas simple ( n = 0 )
if (n == 0):
    print("Le ",n,"ième nombre de fibonacci vaut",0)
else:
    # boucle de calcul pour le cas général
    for i in range(1,n+1):
        fibo = fibo + fiboprecedent
        fiboprecedent = fibo - fiboprecedent
    # affichage résultat
    print("Le ",n,"ième nombre de fibonacci vaut",fibo)

















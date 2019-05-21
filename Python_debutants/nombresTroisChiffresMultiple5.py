# nombresTroisChiffresMultiple5
# ce script affiche la liste des nombres à trois chiffres dont la somme
# des chiffres est multiple de 5
# boucle principale
for n in range(100,1000):
    # on récupère les chiffres
    unite = n % 10
    dizaine = ((n - unite) // 10) % 10
    centaine = (n - 10 * dizaine - unite) // 100
    # on affiche n si la somme des chiffres est multiple de 5
    if ((centaine + dizaine + unite) % 5 == 0):
        print(n)










# 100nombresPremiers
# ce script affiche la liste des 100 premiers nombres premiers
import math
# initialisations
compteur = 0
n = 2
# boucle principale
while (compteur < 100):
    # initialisations
    racineDeN = int(math.sqrt(n))
    diviseur = 2
    # tant qu'on n'a pas trouvé de divisieur, on avance...
    while ((n % diviseur != 0) and (diviseur <= racineDeN)):
        diviseur = diviseur + 1
    # si diviseur est allé au-delà de racineDeN, N est premier
    if (diviseur > racineDeN):
        print(n)
        compteur = compteur + 1
    # on passe à l'entier suivant
    n = n + 1

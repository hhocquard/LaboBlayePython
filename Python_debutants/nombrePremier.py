# nombrePremier
# ce script détermine si l'entier N est premier ou non
import math
# lecture de N
N = int(input("N ? "))
# initialisations
racineDeN = int(math.sqrt(N))
diviseur = 2
# tant qu'on n'a pas trouvé de divisieur, on avance...
while ((N % diviseur != 0) and (diviseur <= racineDeN)):
    diviseur = diviseur + 1
# si diviseur est allé au-delà de racineDeN, N est premier
if (diviseur > racineDeN):
    print ("Le nombre", N, "est premier.")
else:
    print ("Le nombre", N, "est divisible par", diviseur)










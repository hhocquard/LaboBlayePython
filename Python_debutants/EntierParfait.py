# Cet algorithme détermine si un entier N lu au clavier est parfait ou non.
# (un entier est parfait s'il est égal à la somme de ses diviseurs stricts)

# Premiers nombres parfaits : 6, 28, 496, 8 128, 33 550 336, 8 589 869 056
# (le 7 octobre 2008, on ne connaissait que 46 nombres parfaits)

N = int(input ("donnez un entier : "))

somme = 0
for diviseur in range(1,(N//2)+1):
    if (N % diviseur == 0):
        somme = somme + diviseur
        
if (N == somme):
    print (N, "est parfait")
else:
    print (N, "n'est pas parfait - somme des diviseurs =", somme)

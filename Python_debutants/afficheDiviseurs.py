# afficheDiviseurs
# ce script permet d’afficher les diviseurs d’un entier naturel 
# par ordre croissant
# lecture des données
n = int(input("n ? "))
# cas où n est nul
if (n == 0):
    print("Tous les entiers sont diviseurs de 0")
# cas général
else:
    # boucle de parcours, si diviseur divise n, on l’affiche
    for diviseur in range(1,(n // 2)+1):
        if (n % diviseur == 0):
            print(diviseur)
    # dernier diviseur : n
    print(n)












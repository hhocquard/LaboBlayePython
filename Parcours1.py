
###############################################
###  Parcours 1 : ecriture de fonctions simples
###############################################

import math


## Exercice 1 #############################################################
def echanger(L, i, j):
    # cette fonction prend comme arguments une liste L, deux indices
    # valides i et j, et echange dans L les deux elements correspondants. 

    L[i], L[j] = L[j], L[i]
    return L

## La solution ci-dessus ne necessite pas de "variable d'echange".
## Une version "plus classique" est la suivante :
##      ech = L[i]
##      L[i] = L[j]
##      L[j] = ech


## Exercice 2 #############################################################
def inverser(L):
    # cette fonction prend comme argument une liste L et l'inverse
    
    for i in range(len(L) // 2):
        echanger(L, i, len(L) - i - 1)
    return L


## Exercice 3 #############################################################
def moyenne(L):
    # cette fonction prend comme argument une liste non vide de nombres
    # et renvoie la moyenne des elements de cette liste
    
    somme = 0
    for elem in L:
        somme = somme + elem
    return somme / len(L)


## Exercice 4 #############################################################
def maximum(L):
    # cette fonction prend comme argument une liste non vide de nombres
    # et renvoie l'element maximum de cette liste

    maxi = L[0]
    for i in range(1, len(L)):
        if L[i] > maxi:
            maxi = L[i]
    return maxi


## Exercice  5 #############################################################
def indiceMinimum(L): 
    # cette fonction prend comme argument une liste non vide de nombres
    # et renvoie l'indice de l'element minimum de cette liste
    
    indice = 0
    mini = L[0]
    for i in range(1, len(L)):
        if L[i] < mini:
            mini, indice = L[i], i
    return indice
    

## Exercice  6 #############################################################
def triListe(L):
    # cette fonction prend comme argument une liste de nombres L et renvoie
    # une liste triee par ordre croissant contenant les memes elements
    # (sans modifier la liste L)
    #
    # necessite la fonction indiceMinimum

    LT = list(L)
    LR = []
    # on rajoute en fin de LR le plus petit element de LT, que l'on supprime
    # de LT, jusqu'a vider completement LT
    while len(LT) > 0:
        k = indiceMinimum(LT)
        LR.append(LT[k])
        del(LT[k])
    return LR


## Exercice 7 #############################################################
def ecartType(L):
    # cette fonction prend comme argument une serie statistique sous
    # forme d’une liste non vide L de nombres et renvoie l'ecart-type
    # de cette serie
    #
    # necessite la fonction moyenne et le module math

    moy = moyenne(L)
    somme = 0
    for elem in L:
        somme = somme + (elem - moy) ** 2
    ecart = math.sqrt(somme / len(L))
    return ecart

## Remarque : on range la moyenne dans une variable moy pour eviter
## de la recalculer a chaque tour de la boucle for !
## C'est bien plus efficace...


## Exercice 8 #############################################################
def mediane(L):
    # cette fonction prend comme argument une liste non vide de nombres
    # et renvoie la valeur mediane de cette liste
    #
    # necessite la fonction triListe

    LT = triListe(L)
    if len(LT) % 2 == 1:
        indice = (len(LT) - 1) // 2
        med = LT[indice]
    else:
        indice = len(LT) // 2
        med = (LT[indice] + LT[indice - 1]) / 2
    return med


### Exercice  9 #############################################################
def statistiques(L):
    # cette fonction prend comme argument une liste non vide de nombres
    # et renvoie les parametres statistiques (moyenne, ecart-type et mediane)
    # de cette liste
    #
    # necessite les fonctions moyenne, ecartType et mediane
    
    return moyenne(L), ecartType(L), mediane(L)


## Exercice  10 #############################################################
def pairImpair(L):
    # cette fonction prend comme argument une liste de nombres entiers
    # et renvoie deux listes : la premiere liste contient les nombres
    # pairs de L, la seconde les nombres impairs de L
    
    LImpair = []
    LPair = []
    for elem in L:
        if elem % 2 == 0:
            LPair.append(elem)
        else:
            LImpair.append(elem)
    return LPair, LImpair


## Exercice  11 #############################################################
def moinsDeSix(L):
    # cette fonction prend comme argument une liste de mots et renvoie
    # deux listes : la premiere contient les mots de moins de six lettres,
    # la seconde les mots de six lettres ou plus
    
    motsCourts = []
    motsLongs = []
    for elem in L:
        if len(elem) < 6:
            motsCourts.append(elem)
        else:
            motsLongs.append(elem)
    return motsCourts, motsLongs


## Exercice  12 #############################################################
def palindrome(L):
    # cette fonction prend comme argument une liste et verifie si
    # cette liste est un palindrome

    # cas particulier de la liste vide
    if len(L) == 0:
        return True
    # cas general : on verifie la "symetrie" (parcours de la "demi-liste"...))
    # en s'arretant des qu'une anomalie est trouvee
    else:
        for i in range(len(L) // 2):
            if L[i] != L[len(L) - i - 1]:
                return False
        return True
   


## Exercice  13 #############################################################
def diviseurs(nombre):
    # cette fonction prend comme argument un nombre entier et
    # renvoie la liste de ses diviseurs

    LDiviseurs = []
    for i in range(1, nombre + 1):
        if nombre % i == 0:
            LDiviseurs.append(i)
    return LDiviseurs


## 2e version : en ne depassant pas la racine carree...
def diviseursBIS(nombre):
    # cette fonction prend comme argument un nombre entier et
    # renvoie la liste de ses diviseurs
    #
    # necessite le module math

    LDiviseurs = []
    num = 0
    for i in range(1, math.floor(math.sqrt(nombre)) + 1):
        if nombre % i == 0:
            LDiviseurs.insert(num, i)
            if i != nombre // i:
                LDiviseurs.insert(num + 1, nombre // i)
            num = num + 1
    return LDiviseurs



## Exercice  14 #############################################################
def estPremier(nombre):
    # cette fonction prend comme argument un nombre entier et
    # determine si cet entier est premier ou non 

    return len(diviseurs(nombre)) == 2


## Exercice  15 #############################################################
def listeFacteursPremiers(nombre):
    # cette fonction prend comme argument un nombre entier et
    # renvoie la liste de ses facteurs premiers
    #
    # necessite la fonction estPremier

    LDiviseursPremiers = []
    LDiviseurs = diviseurs(nombre)
    for i in range(1, len(LDiviseurs)):
        if estPremier(LDiviseurs[i]):
            LDiviseursPremiers.append(LDiviseurs[i])
    return LDiviseursPremiers


## Exercice  16 #############################################################
def listeChiffres(nombre):
    # cette fonction prend comme argument un entier et renvoie
    # la liste de ses chiffres
    
    if nombre == 0:
        return [0]
    else:
        L = []
        i = nombre
        while i != 0:
            L.insert(0, i % 10)
            i = i // 10
        return L



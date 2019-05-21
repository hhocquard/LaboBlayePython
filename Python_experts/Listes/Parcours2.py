

######################################
###  Parcours 2 : pour aller plus loin
######################################

import math

# fonctions utiles du parcours 1
################################

## Exercice 1
def echanger(L, i, j):
    # cette fonction prend comme arguments une liste L, deux indices
    # valides i et j, et echange dans L les deux elements correspondants.

    L[i], L[j] = L[j], L[i]
    return L


# fonctions du parcours 2
#########################

## Exercice  17 #############################################################
def cleCodeBarre(L):
    # cette fonction prend comme argument une liste constituee
    # des douze premiers chiffres d’un code barre et renvoie la
    # valeur de la cle

    N = 0
    cle = 0
    for i in range(6):
        N = N + L[2 * i] + 3 * L[2 * i + 1]
    if N % 10 != 0:
        cle = 10 - N % 10
    return cle


def estUnCodeBarre(L):
    # cette fonction prend comme argument une liste constituee
    # de treize chiffres et verifie si elle correspond a un
    # code barre valide

    return cleCodeBarre(L) == L[12]


## Exercice  18 #############################################################
def insereElement(L, element):
    # cette fonction prend comme arguments une liste triee et un element
    # et renvoie la liste dans laquelle l’element a ete insere en bonne place

    # on cherche la position d'insertion
    position = 0
    while position < len(L) and L[position] < element:
        position = position + 1
    # on insere dans L
    L.insert(position, element)
    return L


## Exercice  19 #############################################################
def triListeParInsertion(L):
    # cette fonction prend comme argument une liste et renvoie une liste triee
    # par ordre croissant contenant les memes elements
    # algorithme : tri par insertion

    Ltriee = []
    for elem in L:
        Ltriee = insereElement(Ltriee, elem)
    return Ltriee


## Exercice  20 #############################################################
def triListeParEchange(L):
    # cette fonction prend comme argument une liste et la trie par ordre croissant
    # algorithme : tri par echanges
    #
    # necessite la fonction echanger

    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                echanger(L,i,j)
    return L


## Exercice 21 #############################################################
def fusionListes(L1, L2):
    # cette fonction prend comme arguments deux listes triees, construit la liste
    # triee obtenue par fusion de ces deux listes et la renvoie

    # on avance dans L1 avec l'indice ind1, dans L2 avec l'indice ind2
    ind1 = 0
    ind2 = 0
    LTriee = []

    # tant qu'aucune des deux listes a ete entierement traitee, on compare
    # leurs elements et on "garde" le plus petit
    while ind1 < len(L1) and ind2 < len(L2):
        if L1[ind1] < L2[ind2]:
            LTriee.append(L1[ind1])
            ind1 = ind1 + 1
        else:
            LTriee.append(L2[ind2])
            ind2 = ind2 + 1

    # il reste a recopier la fin de la liste non entierement traitee...
    for i in range(ind1, len(L1)):
        LTriee.append(L1[i])
    for i in range(ind2, len(L2)):
        LTriee.append(L2[i])

    # et voila !
    return LTriee

## et maintenant, trions !

def triFusion(L):
    # cette fonction prend comme argument une liste et renvoie une liste triee
    # par ordre croissant contenant les memes elements
    # algorithme : tri par fusion
    #
    # necessite la fonction fusionListes

    LL = list(L)
    # cas simple ?
    if len(LL) <= 1:
        return LL

    # cas general
    # on coupe la liste en deux et on trie les deux moities...
    mil = len(LL) // 2
    L1 = LL[:mil]
    L2 = LL[mil:]
    return(fusionListes(triFusion(L1), triFusion(L2)))


## Exercice 22 #############################################################
def rechercheParDichotomie(L, elem):
    # cette fonction prend comme arguments une liste d’entiers triee L et
    # un entier elem, et renvoie l’indice de cet entier dans la liste, s’il
    # est present, ou la valeur –1 dans le cas contraire
    #
    # algorithme : recherche par dichotomie

    # on utilise deux indices indG et indD (gauche et droit) pour delimiter
    # la "zone de recherche", et un bouleen trouve pour gerer la recherche
    indG = 0
    indD = len(L) - 1
    trouve = False

    # boucle de recherche : arret si trouve ou zone de recherche vide
    while not trouve and indG <= indD:
        # on teste le milieu de la zone de recherche
        milieu = (indG + indD) // 2
        if elem == L[milieu]:
            # on a trouve !
            trouve = True
        elif elem < L[milieu]:
            # on restreint la zone vers la gauche
            indD = milieu - 1
        else:
            # on restreint la zone vers la droite
            indG = milieu + 1

    # resultat final
    if trouve:
        return milieu
    else:
        return -1



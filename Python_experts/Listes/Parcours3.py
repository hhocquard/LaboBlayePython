

##################################
###  Parcours 3 : listes de listes
##################################

import math

# fonction utile du parcours 1
##############################

## Exercice 4
def maximum(L):
    # cette fonction prend comme argument une liste non vide de nombres
    # et renvoie l'element maximum de cette liste

    maxi = L[0]
    for i in range(1, len(L)):
        if L[i] > maxi:
            maxi = L[i]
    return maxi


# fonctions du parcours 3
#########################

## Exercice  23 #############################################################
def moyenneCoeff(L):
    # cette fonction prend comme argument une liste non vide
    # de listes de la forme [ [note1, coef1], [note2, coef2], … ] et renvoie la
    # moyenne de cette liste de notes avec coefficients
    
    sommeCoeffs = 0
    sommeNotesCoeff = 0
    for i in range(len(L)):
        sommeNotesCoeff = sommeNotesCoeff + L[i][0] * L[i][1]
        sommeCoeffs = sommeCoeffs + L[i][1]
    return sommeNotesCoeff / sommeCoeffs


## Exercice  24 #############################################################
def calculeImages(f, a, b):
    # cette fonction prend comme argument une fonction f et deux entiers a et b
    # (avec a ≤ b) et renvoie la liste composee des listes de la forme
    # [x, f(x)], pour x variant de a et b (inclus).
    
    listeImages = []
    for i in range(a, b+1):
        listeImages.append([i, f(i)])
    return listeImages


## Exercice  25 #############################################################
def maximumListeDeListes(L):
    # cette fonction prend comme argument une liste de listes d’elements
    # (contenant au moins un element quelque part…) et renvoie le plus grand
    # element present

    # on cherche la premiere sous-liste non vide, pour initialiser maxi
    i = 0
    while L[i] == []:
        i = i + 1
    maxi = maximum(L[i])

    # on traite les sous-listes suivantes
    for j in range(i+1, len(L)):
        if L[j] != []:
            maxi = max(maxi, maximum(L[j]))
    return maxi

## Une autre version, beacoup plus compacte, utilisant la definition
## de listes en comprehension...
def maximumListeDeListesBIS(L):
    # cette fonction prend comme argument une liste de listes d’elements
    # (contenant au moins un element quelque part…) et renvoie le plus grand
    # element present

    # on renvoie le maximum de la liste des maxima, en ne considerant
    # que les sous-listes non vides
    return(maximum([maximum(elem) for elem in L if len(elem) > 0]))



## Exercice  26 #############################################################
def estMatriceCarree(M):
    # cette fonction verifie si une liste de listes d’entiers M represente
    # ou pas une matrice carree (non vide)
    
    # il faut donc que M soit une liste non vide ne contenant que des
    # sous-listes de meme longueur que M
    longueur = len(M)
    if longueur == 0:
        return False
    for i in range(0, len(M)):
        if len(M[i]) != longueur:
            return False
    return True


## Exercice  27 #############################################################
def matricesSommeCompatibles(M1, M2):
    # cette fonction prend comme arguments deux listes de listes M1 et M2
    # representant deux matrices et determine si leurs dimensions sont identiques

    return len(M1) == len(M2) and len(M1[0]) == len(M2[0])

    
## Exercice  28 #############################################################
def matricesProduitCompatibles(M1, M2):
    # cette fonction prend comme arguments deux listes de listes M1 et M2
    # representant deux matrices et determine si le nombre de colonnes de M1
    # et le nombre de lignes de M2 sont identiques

    return len(M1[0]) == len(M2)
   

## Exercice  29 #############################################################
def produitMatriceParScalaire(M, k):
    # cette fonction prend comme arguments une liste de listes M representant
    # une matrice et un entier k, et renvoie une liste de listes representant le
    # produit de M par k

    MProduit = []
    for i in range(0, len(M)):
        ligne = []
        for j in range(0, len(M[i])):
            ligne.append(k * M[i][j])
        MProduit.append(ligne)
    return MProduit

## la encore, la definition en comprehension permet de proposer une
## version plus compacte :
def produitMatriceParScalaireBIS(M, k):
    # cette fonction prend comme arguments une liste de listes M representant
    # une matrice et un entier k, et renvoie une liste de listes representant le
    # produit de M par k

    return [[k * ligne[i] for i in range(len(ligne))] for ligne in M]


## Exercice  30 #############################################################
def produitLigneColonne(ligne, colonne):
    # cette fonction prend comme arguments une liste ligne et une liste de
    # de listes colonne, et renvoie le produit de ligne par colonne

    produit = 0
    for i in range(len(ligne)):
        produit = produit + ligne[i] * colonne[i][0]
    return produit


def produitMatriceParVecteur(M, V):
    # cette fonction prend comme arguments une liste de listes M representant
    # une matrice et une liste de listes V representant un vecteur colonne,
    # et renvoie une liste de listes representant le produit de cette matrice
    # par ce vecteur
    #
    # necessite la fonction produitLigneColonne

    MProduit = []
    for ligne in M:
         MProduit.append([produitLigneColonne(ligne, V)])
    return MProduit


## Exercice  31 #############################################################
def produitVecteurParMatrice(V, M):
    # cette fonction prend comme arguments une liste representant un vecteur
    # ligne et une liste de listes M representant une matrice, et renvoie une
    # liste de listes representant le produit de ce vecteur par cette matrice

    MProduit = []
    for i in range(len(M[0])):
        produit = 0
        for j in range(len(V)):
            produit = produit + V[j] * M[j][i]
        MProduit.append(produit)
    return MProduit


## Exercice 32 #############################################################
def sommeDeuxLignes(L1, L2):
    # cette fonction prend comme arguments deux listes de meme longueur
    # representant deux lignes de matrices et renvoie une liste representant
    # la somme de ces deux lignes

    return [L1[i] + L2[i] for i in range(len(L1))]
    

def sommeMatrices(M1, M2):
    # cette fonction prend comme arguments deux listes de listes M1 et M2
    # representant deux matrices de meme dimension, et renvoie une liste
    # de listes representant la somme de ces deux matrices

    MSomme = []
    for i in range(len(M1)):
        MSomme.append(sommeDeuxLignes(M1[i], M2[i]))
    return MSomme
    

## Exercice 33 #############################################################
def produitMatrices(M1, M2):
    # cette fonction prend comme arguments deux listes de listes M1 et M2
    # representant deux matrices de dimensions compatibles, et renvoie une
    # liste de listes representant le produit de ces deux matrices

    MProduit = []
    for i in range(len(M1)):
        ligneProduit = []
        for j in range(len(M1)):
            # calcul de l'element val = Mproduit[i][j]
            val = 0
            for k in range(len(M2)):
                val = val + M1[i][k] * M2[k][j]
            # on rajoute val dans la ligne en construction
            ligneProduit.append(val)
        # on rajoute la ligne dans la matrice en construction
        MProduit.append(ligneProduit)
    return MProduit
            
    



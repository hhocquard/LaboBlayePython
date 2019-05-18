
import matplotlib.pyplot as plt


## fonction utile du parcours 3 : pour tester matriceInverse...

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






#################################################
###  Parcours 6 : Pour aller toujours plus loin…
#################################################



## Exercice 47 #############################################################
def transposerMatrice(M):
    # cette fonction prend comme argument une liste de listes M representant
    # une matrice et renvoie une liste de listes representant la transposee
    # de la matrice M

    T = []
    for i in range(len(M[0])):
        # construction de la ligne d'indice i de T
        ligne = []
        for j in range(len(M)):
            ligne.append(M[j][i])
        T.append(ligne)
    return T


## Exercice 48 #############################################################
## determinant d'une matrice

def supprimeLigneColonne(M, i, j):
    # cette fonction prend comme arguments une liste de listes M
    # representant une matrice carree, deux indices i et j, et renvoie
    # une liste de listes representant la matrice M dans laquelle on a
    # supprime la ligne i et la colonne j

    # on recopie M (attention, M est une liste de listes !)
    S = [list(ligne) for ligne in M]
    # on supprime la ligne i dans S
    del(S[i])
    # on supprime la colonne j dans S
    for k in range(len(S)):
        del(S[k][j])
    return S


def determinantMatrice(M):
    # cette fonction prend comme argument une liste non vide de listes M
    # representant une matrice carree et renvoie le determinant de cette
    # matrice
    #
    # necessite la fonction supprimeLigneColonne

    if len(M) == 1:
        return M[0][0]
    else:
        det = 0
        # on calcule le determinant par rapport a la 1re ligne
        signe = 1
        for j in range(len(M)):
            det = det + signe * M[0][j] * determinantMatrice(supprimeLigneColonne(M, 0, j))
            signe = - signe
        return det


## Exercice 49 #############################################################
def comatrice(M):
    # cette fonction prend comme argument une liste non vide de listes M
    # representant une matrice carree et renvoie la comatrice de cette
    # matrice
    #
    # necessite les fonctions supprimeLigneColonne et determinantMatrice

    # on initialise la comatrice C a 0 partout
    C = [ [0 for y in M ] for x in M ]
    # on calcule les coefficients de C
    for i in range(len(C)):
        for j in range(len(C)):
            C[i][j] = ((-1) ** (i + j)) * determinantMatrice(supprimeLigneColonne(M, i, j))
    return C        




## Exercice 50 #############################################################
def matriceInverse(M):
    # cette fonction prend comme argument une liste non vide de listes M
    # representant une matrice carree et renvoie la matrice inverse de cette
    # matrice
    #
    # necessite les fonctions transposerMatrice, comatrice et determinantMatrice

    I = transposerMatrice(comatrice(M))
    det = determinantMatrice(M)
    for i in range(len(I)):
        for j in range(len(I)):
            I[i][j] = I[i][j] / det
    return I
    


## Exercice 51 #############################################################
## Points alignes

def deter(A, B, C):
    # cette fonction prend comme arguments trois listes representant les
    # coordonnees de trois points A, B et C, et renvoie la valeur de l'expression
    # (XB - XA)(YC - YA) - (YB - YA)(XC - XA)

    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

def pointsAlignes(A, B, C):
    # cette fonction prend comme arguments trois listes representant les
    # coordonnees de trois points A, B et C, et determine si ces points sont on non
    # alignes
    #
    # necessite la fonction deter

    return deter(A, B, C) == 0


## Exercice 52 #############################################################
def enPositionGenerale(L):
    # cette fonction prend comme argument une liste de listes representant
    # les coordonnees d'un ensemble de points et determine si ces points sont
    # ou non en position generale
    #
    # necessite la fonction pointsAlignes

    if len(L) >= 3:
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                for k in range(j + 1, len(L)):
                    if pointsAlignes(L[i], L[j], L[k]):
                        return False
    return True


## Exercice 53 #############################################################
## Polygone convexe ?

def memeCote(L, i, j):
    # cette fonction prend comme arguments une liste de listes representant
    # les coordonnees d'un ensemble de points P1, ..., Pn et deux indices i et j,
    # puis determine si tous les points autres que Pi Pj sont du meme cote de
    # la droite determinee par ces deux points
    #
    # necessite la fonction deter

    # on commence par determiner le signe de deter, en cherchant le premier
    # dont la valeur est non nulle...
    k = 0
    trouve = False
    while k < len(L) and not trouve:
        if (k != i) and (k != j):
            det = deter(L[i], L[j], L[k])
            if det != 0:
                trouve = True
            else:
                k = k + 1
        else:
            k = k + 1

    # si les deter n'etaient pas tous nuls...                
    if trouve:
        estPositif = det > 0
        # on verifie que tous les autres deter sont de meme signe
        # si on trouve un signe different on renvoie False
        for kk in range(k + 1, len(L)):
            if (kk != i) and (kk != j):
                if estPositif != (deter(L[i], L[j], L[kk]) > 0):
                    return False
            kk = kk + 1

    # on a tout verifie, c'est donc ok
    return True



def polygoneConvexe(L):
    # cette fonction prend comme argument une liste de listes representant
    # les coordonnees d'un ensemble de points et determine si le polygone defini
    # par cet ensemble de points est ou non convexe
    #
    # necessite la fonction memeCote

    # on commence par tester le couple (P1,Pn)
    ok = memeCote(L, 0, len(L) - 1)

    # on teste les autres paires, mais on s'arrete des que ok vaut False
    i = 0
    while ok and i < len(L) - 1:
        ok = memeCote(L, i, i + 1)
        i = i + 1

    return ok
    


## Exercice 54 #############################################################
## Interpolation de Lagrange

def abscisseMinimale(L):
    # cette fonction prend comme argument une liste de listes representant
    # les coordonnees d'un ensemble de points et renvoie l'abscisse minimale
    # de ces points

    m = L[0][0]
    for i in range(1,len(L)):
        m = min(m, L[i][0])
    return m


def abscisseMaximale(L):
    # cette fonction prend comme argument une liste de listes representant
    # les coordonnees d'un ensemble de points et renvoie l'abscisse maximale
    # de ces points

    m = L[0][0]
    for i in range(1,len(L)):
        m = max(m, L[i][0])
    return m


def polynomeLagrange(L, i, x):
    # cette fonction prend comme argument une liste de listes representant
    # les coordonnees d'un ensemble de points, un entier i et un flottant x,
    # et renvoie la valeur en x du i-ieme polynome de Lagrange associe
    # a ces points

    produit = 1
    for j in range(len(L)):
        if j != i:
            produit = produit * (x - L[j][0]) / (L[i][0] - L[j][0])

    return produit


def polynomeInterpolation(L, x):
    # cette fonction prend comme argument une liste de listes representant
    # les coordonnees d'un ensemble de points et un flottant x, et renvoie
    # la valeur en x du polynome d'interpolation associe a ces points
    #
    # necessite la fonction polynomeLagrange

    somme = 0
    for i in range(len(L)):
        somme = somme + L[i][1] * polynomeLagrange(L, i, x)

    return somme

def dessineLagrange(L, i, a, b):
    # cette fonction prend comme argument une liste de listes representant
    # les coordonnees d'un ensemble de points, un entier i et deux flottants
    # a et b, et dessine la courbe du i-ieme polynome de Lagrange associe
    # a ces points sur l'intervalle [a ; b]
    #
    # necessite la fonction polynomeLagrange et le module matplotlib.pyplot

    plt.plot(L[i][0], L[i][1], 'o', ms=10, mfc='w')
    nbPoints = (b - a) * 100
    LX = [ a + x * (b - a) / nbPoints for x in range(nbPoints) ]
    LY = [ L[i][1] * polynomeLagrange(L, i, x) for x in LX ]
    plt.plot(LX,LY,"--")

    
def dessineInterpolation(L, a, b):
    # cette fonction prend comme argument une liste de listes representant
    # les coordonnees d'un ensemble de points et deux flottants a et b, et
    # dessine la courbe du polynome d'interpolation associe a ces points
    # sur l'intervalle [a ; b]
    #
    # necessite la fonction polynomeInterpolation et le module matplotlib.pyplot

    nbPoints = (b - a) * 100
    LX = [ a + x * (b - a) / nbPoints for x in range(nbPoints) ]
    LY = [ polynomeInterpolation(L, x) for x in LX ]
    plt.plot(LX,LY,'k-',lw=3)

    
def representationLagrange(L):
    # cette fonction prend comme argument une liste de listes representant
    # les coordonnees d'un ensemble de points, puis dessine les courbes
    # des polynomes de Lagrange associees a ces points ainsi que la courbe
    # du polynome d'interpolation 
    #
    # necessite les fonctions abscisseMinimale, abscisseMaximale,
    # dessineLagrange et dessineInterpolation, ainsi que le module
    # matplotlib.pyplot
        
    # limites du rectangle pour les courbes
    miniX = abscisseMinimale(L) - 1
    maxiX = abscisseMaximale(L) + 1

    # dessin des points et des courbes de Lagrange
    for i in range(len(L)):
        dessineLagrange(L, i, miniX, maxiX)

    # dessin de l'interpolation
    dessineInterpolation(L, miniX, maxiX)

    # on recupere les limites du dessin pour dessiner les axes
    D = plt.axis()
    # dessin des axes en noir
    plt.plot([0,0], [D[2], D[3]], "k-")
    plt.plot([D[0], D[1]], [0,0], "k-")
    
    plt.show()

# une liste de quatre points pour tester...
L = [ [-9,5], [-4,2], [-1,-2], [7,9] ]



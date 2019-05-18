
###############################################
###  Parcours 4 : Graphiques, exercices de base
###############################################

import math
import random
import matplotlib.pyplot as plt


## Une petite fonction qui permet de dessiner les axes du repere
## centres sur le point de coordonnees (0;0)
## Natruellement, si ce point n'est pas dans la fenetre de visualisation,
## le repere ne sera pas visible
##
## cette fonction doit etre appelee juste avant le plt.show() :
##    axecentre()
##    plt.show()
##
def repereCentre ():
    # on recupere les coordonnees de la fenetre dans la liste f
    f = plt.axis()
    # on recupere les axes pour les deplacer...
    ax=plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))

## Exercice 34 #############################################################
def dessineMaison():
    # cette fonction dessine une "maison"
    #
    # necessite le module matplotlib.pyplot

    # les murs (rectangle)
    LX = [0, 5, 5, 0, 0]
    LY = [0, 0, 3, 3, 0]
    plt.plot(LX, LY, "-k")
    # le toit (pointe)
    LX = [0, 2.5, 5]
    LY = [3, 4, 3]
    plt.plot(LX, LY, "-k")
    # la porte
    LX = [1, 1, 2, 2]
    LY = [0, 2, 2, 0]
    plt.plot(LX, LY, "-k")
    # la fenetre
    LX = [3, 3, 4, 4, 3]
    LY = [1, 2, 2, 1, 1]
    plt.plot(LX, LY, "-k")

    plt.title("La petite maison dans la fenetre")
    plt.grid()
    plt.show()


def dessineMaisonBIS():
    # cette fonction dessine une "maison" avec la porte bleue
    # et la fenetre rouge...
    #
    # necessite le module matplotlib.pyplot

    # les murs (rectangle)
    LX = [0, 5, 5, 0, 0]
    LY = [0, 0, 3, 3, 0]
    plt.plot(LX, LY, "-k")
    # le toit (pointe)
    LX = [0, 2.5, 5]
    LY = [3, 4, 3]
    plt.plot(LX, LY, "-k")
    # la porte
    LX = [1, 1, 2, 2]
    LY = [0, 2, 2, 0]
    plt.plot(LX, LY, "-b")
    # la fenetre
    LX = [3, 3, 4, 4, 3]
    LY = [1, 2, 2, 1, 1]
    plt.plot(LX, LY, "-r")

    plt.title("La petite maison dans la fenetre")
    plt.grid()
    plt.show()


## Exercice 35 #############################################################
def dessinePolygone(LS):
    # cette fonction prend comme argument une liste non vide LS de listes
    # representant les coordonnees des sommets d’un polygone, et dessine
    # ce polygone
    #
    # necessite le module matplotlib.pyplot

    LX = [sommet[0] for sommet in LS]
    LY = [sommet[1] for sommet in LS]
    # on rajoute le 1er sommet en fin de liste, pour que le polygone soit ferme
    LX.append(LX[0])
    LY.append(LY[0])
    plt.plot(LX, LY, "r-", linewidth = 2)
    plt.show()


## Exercice 36 #############################################################
def schemaDeverouillage(L):
    # cette fonction prend comme argument une liste de listes représentant un
    # schéma de déverrouillage de smartphone et le dessine
    #
    # necessite le module matplotlib.pyplot

    # repere orthonorme mais non dessine...
    plt.axis("equal")
    plt.axis("off")
    
    # dessin des neufs points
    Lx = 3 * [0] + 3 * [1] + 3 * [2]
    Ly = 3 * [0, 1, 2]
    plt.plot(Lx, Ly, "ok", ms = 20)

    # dessin du schema
    Lx = [ elem[0] for elem in L ]
    Ly = [ elem[1] for elem in L ]
    plt.plot(Lx, Ly, "-k", lw = 10)
    
    plt.show()

# une liste pour tester...
SCHEMA = [ [0, 0], [0, 1], [2, 1], [2, 2], [1, 0], [0, 2] ]


## Exercice 37 #############################################################
#
# La fonction queFaitElle trace la courbe representative de la fonction
# sinus sur l'intervalle [-4 ; 4]


## Exercice 38 #############################################################
def traceCourbeCosinus(n, a, b):
    # cette fonction prend comme arguments un entier n, deux entiers a et b
    # avec a < b, et trace la courbe de la fonction cosinus sur l’intervalle
    # [a ; b] a l’aide de n points
    #
    # necessite les modules math et matplotlib.pyplot

    LX = [a + x * (b - a) / (n - 1) for x in range(n)]
    LY = [math.cos(x) for x in LX]
    plt.axis('equal')
    plt.plot(LX, LY, "r-", linewidth = 2)
    repereCentre()
    plt.show()
    

## Exercice 39 #############################################################
def f(x):
    # une simple fonction exemple, pour pouvoir tester
    return (x + 5) / (2 * x + 4)


def traceCourbeFonction(f, n, a, b):
    # cette fonction prend comme arguments une fonction f, un entier n, deux
    # entiers a et b avec a < b, et trace la courbe de la fonction f sur
    # l’intervalle [a ; b] a l’aide de n points
    #
    # necessite le module matplotlib.pyplot

    LX = [a + x * (b - a) / (n - 1) for x in range(n)]
    LY = [f(x) for x in LX]
    plt.axis('equal')
    plt.plot(LX, LY, "r-", linewidth = 2)
    plt.show()



    
    


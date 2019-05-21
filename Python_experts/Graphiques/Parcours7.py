
##################################
###  Parcours 7 : Gestion de stock
##################################

## Une proposition de representation
## Les listes necessaires

# les produits proposes
lampes = ['L1', 'L2', 'L3']

# les pieces necessaires
pieces = ['LED', 'halogene', 'douille simple', 'douille multiple',
              'gradateur', 'interrupteur simple']

# les quantites de pieces en stock
stock = [150, 220, 224, 331, 214, 39]

# les protocoles de fabrication
# p.ex. [2, 0, 3] : en position 0 donc concerne les LED
# il en faut 2 pour une lampe L1, aucune pour L2 et 3 pour L3
protocoles = [[2, 0, 3], [0, 4, 2], [2, 0, 0], [0, 2, 2], [0, 2, 0], [1, 0, 1]]
# remarque : on aurait pu naturellement avoir, de facon equivalente, trois
# sous-listes de taille 6...



## Les fonctions demandees


## 1. mettre a jour le stock a partir d’une livraison reçue
def miseaJourStockAjout(listeLivraison, stock):
    # modifie le stock en ajoutant toutes les pieces livrees
    # listeLivraison donne la quantite recue de chaque piece

    for i in range(len(stock)):
            stock[i] = stock[i] + listeLivraison[i]
    # note : la liste stock est modifiee, pas besoin de return...


## 2. savoir combien de lampes d’un type donne il est possible de
##    fabriquer en fonction du stock de pieces disponible
def combien(typeLampe, lampes, stock, protocoles):
    # renvoie le nombre de lampes du type typeLampe qui peuvent etre fabriquees
    # en fonction du stock actuel

    # ind = index de la lampe concernee
    ind = lampes.index(typeLampe)

    # on cherche la premiere piece necessaire dans protocoles
    # c'est-a-dire celle dont la quantite correspondante est non nulle
    i = 0
    while protocoles[i][ind] == 0:
        i = i + 1

    # initialisation du minimum
    nbreLampes = stock[i] // protocoles[i][ind]
    
    # on regarde chaque piece necessaire pour mise a jour minimum...
    for k in range(i + 1, len(protocoles)):
        if protocoles[k][ind] != 0:
            nbreLampes = min(nbreLampes, stock[k] // protocoles[k][ind])

    return nbreLampes


## 3. savoir si une commande est realisable, en fonction du stock
##    de pieces disponible
def besoinsCommande(listeNbreLampes, protocoles):
    # renvoie une liste donnant la quantite de chaque piece necessaire
    # pour realiser la commande de lampes donnee par listeNbreLampes

    besoins = []
    for i in range(len(protocoles)):
        quantite = 0
        for j in range(len(listeNbreLampes)):
            quantite = quantite + listeNbreLampes[j] * protocoles[i][j]
        besoins.append(quantite)

    return besoins


def commandeEstRealisable(listeNbreLampes, stock, protocoles):
    # renvoie True si la commande de lampes donnee par listeNbreLampes
    # est realisable dans l'etat actuel des stocks et False sinon.
    #
    # necessite la fonction besoinsCommande
    
    besoins = besoinsCommande(listeNbreLampes, protocoles)
    for i in range(len(stock)):
        if besoins[i] > stock[i]:
            return False
    return True


## 4. connaitre le reapprovisionnement necessaire (quantite de
##    pieces à commander) pour realiser une commande actuellement
##    non realisable
def reassortCommande(listeNbreLampes, stock, protocoles):
    # renvoie la liste des quantites de pieces a commander pour realiser
    # la commande de lampes donnee par listeNbreLampes
    #
    # necessite la fonction besoinsCommande

    besoins = besoinsCommande(listeNbreLampes, protocoles)
    return [max(0, besoins[i] - stock[i]) for i in range(len(stock))]



## 5. mettre a jour le stock a partir d’une commande realisable
##    (les pieces necessaires a la fabrication sont retirees du stock),
def miseaJourStockRetrait(listeNbreLampes, stock, protocoles):
    # modifie le stock en retirant toutes les pieces necessaires a la
    # realisation de la commande de lampes donnee par listeNbreLampes
    #
    # necessite la fonction besoinsCommande

    besoins = besoinsCommande(listeNbreLampes, protocoles)
    for i in range(len(stock)):
            stock[i] = stock[i] - besoins[i]
    # note : la liste stock est modifiee, pas besoin de return...



## 6. rajouter un nouveau type de lampe au catalogue, ainsi que
##    le protocole de fabrication associe
def ajoutLampe(nomLampe, nouveauProtocole, lampes, stock, protocoles):
    # rajoute un type de lampe au catalogue ainsi que son protocole

    # la nouvelle lampe
    lampes.append(nomLampe)
    # le nouveau protocole (rajout en fin de toutes les sous-listes)
    for i in range(len(protocoles)):
        protocoles[i].append(nouveauProtocole[i])
    # stock a zero
    stock.append(0)
    
    
    



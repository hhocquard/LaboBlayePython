
#############  import  ###################
##########################################

import PIL.Image as PIL
import math

##########################################
##########################################

# creation d'une image "noire" et chargement de l'image teapot
monImage = PIL.new("RGB", (300, 200))
teapot = PIL.open("teapot.png")


########### Question 2 ###################

def ligneHorizontaleBlancheAuMilieu(img):
    # dessine une ligne horizontale
    # blanche au milieu de l'image img

    l, h = img.size
    for x in range(l):
        PIL.Image.putpixel(img, (x, h // 2), (255, 255, 255))

#ligneHorizontaleBlancheAuMilieu(teapot)
#PIL.Image.show(teapot)


########### Question 3 ###################

def ligneHorizontaleAuMilieu(img, c):
    # dessine une ligne horizontale au milieu de
    # l'image img en choisissant la couleur de la
    # ligne lors de l'appel

    l, h = img.size
    for x in range(l):
        PIL.Image.putpixel(img, (x, h // 2), c)

#ligneHorizontaleAuMilieu(monImage,(255,0,0))
#PIL.Image.show(monImage)


########### Question 4 ###################

def ligneHorizontale(img, c, y):
    # dessine, dans une image img donnee
    # une ligne horizontale de couleur c
    # a la distance y du haut de l'image

    l, h = img.size
    for x in range(l):
        PIL.Image.putpixel(img, (x, y), c)


#ligneHorizontale(monImage,(255,0,0),10)
#PIL.Image.show(monImage)

def ligneHorizontaleAuMilieu2(img,c):
    # 2e version
    l, h = img.size
    ligneHorizontale(img,h//2,c)


########### Question 5 ###################

def grilleHorizontale(img, c, d):
    # dessine une grille de lignes horizontales
    # espacees de d - 1 pixels

    l, h = img.size
    for y in range(0, h, d):
        ligneHorizontale(img, c, y)

##grilleHorizontale(monImage,(255, 0, 0), 5)
##PIL.Image.show(monImage)


########### Question 6 ###################

def diagonale(img):
    # dessine en blanc une diagonale sur l'image

    l, h = img.size
    if l > h:
        for x in range(l):
            PIL.Image.putpixel(img, (x, (h * i) // l), (255, 255, 255))
    else:
        for y in range(h):
            PIL.Image.putpixel(img, ((l * i) // h, y), (255, 255, 255))

##diagonale(monImage)
##PIL.Image.show(monImage)


########### Question 7 ###################

def cercle(img, x, y, r):
    # dessine en blanc un cercle ayant pour centre le point M(x;y)

    nbpoints = (int) (2 * math.pi * r)
    for i in range(nbpoints):
        ptx = x + r * math.cos(i * 2 * math.pi / nbpoints)
        pty = y + r * math.sin(i * 2 * math.pi / nbpoints)
        PIL.Image.putpixel(img, (int(ptx), int(pty)), (255, 255, 255))
    PIL.Image.show(img)
##cercle(teapot, 50, 50, 30)
##PIL.Image.show(teapot)


########### Question 8 ###################

def filtreRouge(img):
    # ne conserve que la composante rouge de l'image

    l, h = img.size
    for x in range(l):
        for y in range(h):
            (r, g, b) = PIL.Image.getpixel(img, (x, y))
            PIL.Image.putpixel(img, (x, y), (r, 0, 0))


def filtreVert(img):
    # ne conserve que la composante verte de l'image

    l, h = img.size
    for x in range(l):
        for y in range(h):
            (r, g, b) = PIL.Image.getpixel(img, (x, y))
            PIL.Image.putpixel(img, (x, y), (0, g, 0))


def filtreBleu(img):
    # ne conserve que la composante bleue de l'image

    l, h = img.size
    for x in range(l):
        for y in range(h):
            (r, g, b) = PIL.Image.getpixel(img, (x, y))
            PIL.Image.putpixel(img, (x, y), (0, 0, b))


def filtres(img):
    # produit une image contenant img et les trois images filtrees
    # cote a cote...

    l, h = img.size
    imgCopie = PIL.new("RGB", (l, h))
    imgGlobal = PIL.new("RGB", (4 * l, h))

        # image initiale
    imgGlobal.paste(img, [0, 0])
        # filtre rouge
    imgCopie.paste(img, [0, 0])
    filtreRouge(imgCopie)
    imgGlobal.paste(imgCopie, [l, 0])
        # filtre vert
    imgCopie.paste(img, [0, 0])
    filtreVert(imgCopie)
    imgGlobal.paste(imgCopie, [2 * l, 0])
        # filtre bleu
    imgCopie.paste(img, [0, 0])
    filtreBleu(imgCopie)
    imgGlobal.paste(imgCopie, [3 * l, 0])
        # affichage image resultat
    PIL.Image.show(imgGlobal)

teapot = PIL.open("teapot.png")
filtres(teapot)


########### Question 9 ###################

def modifierLuminosite(img, facteur):
    # modifie la luminosite de img en multipliant
    # chaque composante (r, g, b) par facteur

    l, h = img.size
    for x in range(l):
        for y in range(h):
            (r, g, b) = PIL.Image.getpixel(img, (x, y))
            PIL.Image.putpixel(img, (x, y),
                (math.floor(r * facteur),
                 math.floor(g * facteur),
                 math.floor(b * facteur)))

##teapot = PIL.open("teapot.png")
##modifierLuminosite(teapot,1.5)
##PIL.Image.show(teapot)
##modifierLuminosite(teapot,0.5)
##PIL.Image.show(teapot)


########### Question 10 ###################

def monochrome1(img):
    # repeint chaque pixel de couleur (r, g, b) en (m, m, m)
    # avec m = (r + g + b) // 3

    l, h = img.size
    for x in range(l):
        for y in range(h):
            (r, g, b) = PIL.Image.getpixel(img, (x, y))
            m = (r + g + b) // 3
#            v = int(0.3 * r + 0.59 * g + 0.11 * b)
            PIL.Image.putpixel(img, (x, y), (m, m, m))


def monochrome2(img):
    # repeint chaque pixel de couleur (r, g, b) en (m, m, m)
    # avec m = math.floor(0.3 * r + 0.59 * g + 0.11 * b)

    l, h = img.size
    for x in range(l):
        for y in range(h):
            (r, g, b) = PIL.Image.getpixel(img, (x, y))
            m = math.floor(0.3 * r + 0.59 * g + 0.11 * b)
            PIL.Image.putpixel(img, (x, y), (m, m, m))

##teapot = PIL.open("teapot.png")
##monochrome1(teapot)
##PIL.Image.show(teapot)
##teapot = PIL.open("teapot.png")
##monochrome2(teapot)
##PIL.Image.show(teapot)


########### Question 11 ###################

def noirEtBlanc(img):
    # convertit en noir et blanc la version monochrome de img

    l, h = img.size
    for x in range(l):
        for y in range(h):
            (r, g, b) = PIL.Image.getpixel(img, (x, y))
            if (r + g + b) >= 3 * 127:
                PIL.Image.putpixel(img, (x, y),(255, 255, 255))
            else:
                PIL.Image.putpixel(img, (x, y),(0, 0, 0))

##teapot = PIL.open("teapot.png")
##noirEtBlanc(teapot)
##PIL.Image.show(teapot)


########### Question 12 ###################


def posteriser(img, n):
    # arrondit les composantes r, g, b de img a un multiple de n

    l, h = img.size
    for x in range(l):
        for y in range(h):
            (r, g, b) = PIL.Image.getpixel(img, (x, y))
            PIL.Image.putpixel(img, (x, y), (r // n * n, g // n * n, b // n * n))

##teapot = PIL.open("teapot.png")
##posteriser(teapot,64)
##PIL.Image.show(teapot)
##teapot = PIL.open("teapot.png")
##posteriser(teapot,128)
##PIL.Image.show(teapot)
##teapot = PIL.open("teapot.png")
##posteriser(teapot,150)
##PIL.Image.show(teapot)
##teapot = PIL.open("teapot.png")
##posteriser(teapot,200)
##PIL.Image.show(teapot)


########### Question 13 ###################

def flou(img):
    # renvoie une image floue de img en peignant chaque
    # pixel non au bord par la couleur moyenne des pixels voisins

    l, h = img.size
    imgFloue = PIL.new("RGB", (l, h))
    for x in range(1, l - 1):
        for y in range(1, h - 1):
            (r, g, b) = (0, 0, 0)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    (r2, g2, b2) = PIL.Image.getpixel(img, (x + i, y + j))
                    r = r + r2
                    g = g + g2
                    b = b + b2
            r = r // 9
            g = g // 9
            b = b // 9
            PIL.Image.putpixel(imgFloue, (x, y), (r, g, b))
    return imgFloue


##teapot = PIL.open("teapot.png")
##PIL.Image.show(teapot)
##teapot = flou(teapot)
##PIL.Image.show(teapot)


########### Question 14 ###################

def miroirVertical(img):
    # renvoie le miroir vertical de l'image img

    l, h = img.size
    imgMiroirV = PIL.new("RGB", (l, h))
    for x in range(l):
        for y in range(h):
            c = PIL.Image.getpixel(img, (x, y))
            PIL.Image.putpixel(imgMiroirV, (x, h - 1 - y), c)
    return imgMiroirV


def miroirHorizontal(img):
    # renvoie le miroir horizontal de l'image img

    l, h = img.size
    imgMiroirH = PIL.new("RGB", (l, h))
    for x in range(l):
        for y in range(h):
            c = PIL.Image.getpixel(img,(x, y))
            PIL.Image.putpixel(imgMiroirH,(l - 1 - x, y),c)
    return imgMiroirH


##teapot = PIL.open("teapot.png")
##PIL.Image.show(miroirVertical(teapot))
##PIL.Image.show(miroirHorizontal(teapot))


########### Question 15 ###################

def rotation90(img):
    # renvoie l'image img tournee de 90 degres dans le sens horaire

    l, h = img.size
    imgRot = PIL.new("RGB", (h, l))
    for x in range(l):
        for y in range(h):
            (r, g, b) = PIL.Image.getpixel(img, (x, y))
            PIL.Image.putpixel(imgRot, (h - y - 1, x), (r, g, b))
    return imgRot


##teapot = PIL.open("teapot.png")
##PIL.Image.show(rotation90(teapot))


########## Question 16 #####################

def rotationImage(img, angle):
    # renvoie l'image img tournee de angle radians dans le sens horaire

    l, h = img.size
    origine = math.floor(math.sqrt(l ** 2 + h ** 2)) + 1
    maxRot = 2 * origine
    imgRot = PIL.new("RGB", (maxRot, maxRot))

    for x in range(maxRot):
        for y in range(maxRot):
            xx = x - origine
            yy = y - origine
            xImg = math.floor(xx * math.cos(angle) + yy * math.sin(angle))
            yImg = math.floor(-xx * math.sin(angle) + yy * math.cos(angle))
            if xImg >= 0 and xImg < l and yImg >= 0 and yImg < h:
                (r, g, b) = PIL.Image.getpixel(img, (xImg, yImg))
                PIL.Image.putpixel(imgRot, (x, y), (r, g, b))
    return imgRot


##teapot = PIL.open("teapot.png")
##PIL.Image.show(teapot)
##PIL.Image.show(rotationImage(teapot, math.pi/8))
##PIL.Image.show(rotationImage(teapot, math.pi/6))
##PIL.Image.show(rotationImage(teapot, math.pi/3))
##PIL.Image.show(rotationImage(teapot, 2*math.pi/3))


# équationDroite
# Ce script détermine l’équation d’une droite donnée par deux de
# ses points
# lecture données
XA = float(input("XA : "))
YA = float(input("YA : "))
XB = float(input("XB : "))
YB = float(input("YB : "))
# cas particulier : XA = XB
if ( XA == XB ):
    print( "équation de la droite : x = ", XA )
# cas général
else:
    # calcul du coefficient directeur
    coef = ( YA - YB ) / ( XA - XB )
    # calcul de l’ordonnée à l’origine
    cste = YA - coef * XA
    # affichage résultat
    print ( "équation de la droite : y = ", coef, "x + ", cste )




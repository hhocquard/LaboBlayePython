# équationDroiteParallèle
# Ce script détermine l’équation d’une droite passant par A et
# parallèle à un segment BC
# lecture données
XA = float(input("XA : "))
YA = float(input("YA : "))
XB = float(input("XB : "))
YB = float(input("YB : "))
XC = float(input("XC : "))
YC = float(input("YC : "))
# cas particulier 1 : XB = XC
if ( XB == XC ):
    print( "équation de la droite : x = ", XA )
# cas particulier 2 : YB = YC
elif ( YA == YB ):
    print( "équation de la droite : y = ", YA )
# cas général
else:
    # calcul du coefficient directeur
    coef = ( YB - YC ) / ( XB - XC )
    # calcul de l’ordonnée à l’origine
    cste = YB - coef * XB
    # affichage résultat
    print ( "équation de la droite : y = ", coef, "x + ", cste )





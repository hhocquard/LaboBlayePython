# sommeDeDeuxFractions
# ce script calcule le numérateur et le dénominateur d’une somme 
# de deux fractions entières.
# lecture données
numA = int(input("numérateur A : "))
denomA = int(input("dénominateur A : "))
numB = int(input("numérateur B : "))
denomB = int(input("dénominateur B : "))
# calcul d’un dénominateur commun
denomSomme = denomA * denomB
# calcul du numérateur
numSomme = (numA * denomB) + (numB * denomA)
# affichage résultat
print("la somme vaut",numSomme,"/",denomSomme)

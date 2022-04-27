"""Écrire, une fonction Python appelée compte_a qui prend en entrée une chaîne S non vide 
contenant des caractères: 'a', '3', 'y', 'z'...
La fonction doit imprimer :
- le nombre du caractère a présent dans la chaine.
- La longueur de la chaine
- Le pourcentage de ce nombre arrondi à 1 décimale
Indication :
La fonction count compte le nombre de caractères dans une chaine.
La fonction round(nombre, digits) arrondit le nombre au nombre de digits.
Exemple :
S=("abcaa")
nbreA=s.count("a")
print(nbreA) affichera 3
x= round(5.76543, 2)
print(x) affichera 5.7"""

def compte_a(S,a):
    l=len(S)
    compte= S.count(a)
    pourc= (compte/l)*100
    pourc=round(pourc,1)

    return l,compte, pourc

s="Abc58"
print(compte_a(s,"a"))

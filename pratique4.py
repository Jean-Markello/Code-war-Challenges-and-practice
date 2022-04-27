"""Écrire une fonction imp_div9 qui ne prend pas de paramètre. La fonction doit demander à 
l’utilisateur de rentrer un entier positif. La fonction doit renvoyer True si l’élément fourni
est impair et divisible par 9 et False sinon.
Exemple de deux exécutions :
Entrer un nombre positif :109
False
Entrer un nombre positif :99
True
"""

def imp_div9():
    while True:
        x=int(input("Entrer un entier positif: "))
        if x>0:
            break
    if x%2!=0 and x%9==0:
        return True
    else:
        return False

print(imp_div9())

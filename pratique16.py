"""Question 1 :
Écrire une fonction Python appelée mon_Entier qui prend en entrée un entier, n où n est un 
entier positif avec 3 chiffres. Votre fonction ne sera testée qu'avec de tels entiers n.
La fonction doit renvoyer le chiffre du milieu de n. 
Exemple de deux exécutions :
>>> print(mon_Entier(523))
2
"""
def mon_Entier(x):
    x=str(x)
    return x[1]

print(mon_Entier(523))

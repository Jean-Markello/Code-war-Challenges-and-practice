"""Écrire une fonction Python appelée somme qui prend en entrée une chaîne s. La chaîne s 
n'a que les chiffres 0 à 9 comme caractères et sa longueur est non nulle. Votre fonction 
ne sera testée qu'avec de telles chaînes. La fonction renvoie la somme des chiffres 
contenus dans s.
Exemple d’exécutions :
n = somme('10335092')
print(n) affichera 23"""

def somme(s):
    b=0
    s= [int(v) for v in s]
    for x in s:
        b+=x
    return b

s='10335092'
print(somme(s))


"""Question 5 :
Écrire une fonction Python appelée affiche qui prend en entrée une chaîne s. La chaîne s 
n'a que les chiffres 0 à 9 comme caractères et sa longueur est non nulle. Votre fonction 
ne sera testée qu'avec de telles chaînes.
Votre fonction doit produire une nouvelle chaine composée des caractères se trouvant 
dans les positions 1, 4, 7,.. de s et afficher cette nouvelle chaine.
Par exemple s= '1035587982', la nouvelle chaine sera 059 """

def coupe(d):
    n=""
    l=len(d)
    for i in range(1,l, 3):
        n+=d[i:i+1]
    return n


s= '1035587982'
print(coupe(s))
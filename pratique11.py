"""Créez une fonction move_zeros qui prend comme paramètre une liste des entiers et 
déplace tous les zéros à la fin de la liste. Par exemple, si la liste est [1, 0, 3, 0, 0, 5, 7] le 
résultat devrait être [1, 3, 5, 7, 0, 0, 0]
Préparez TROIS solutions
• move_zeros_v1 utilise une autre liste tmp pour calculer la nouvelle liste et la retourne 
comme résultat (problème facile) . La liste initiale n’est pas changée.
• move_zeros_v2 modifies la liste initiale à l’intérieur de la fonction. La fonction ne 
retourne rien.
• move_zeros_v3 déplace les éléments dans la liste initiale sans utiliser des listes 
temporaires (probleme plus difficile). La fonction ne retourne rien. On peut utiliser 
une variable temporaire pour échanger deux éléments, mais on peut utiliser l’échange 
Python a,b=b,"""


def move_zeros_v1(p):
    tmp=[]
    l=p.count(0)
    for x in p:
        if x!=0:
            tmp.append(x)
    for b in range(l):
        tmp.append(0)
    return tmp

def move(l):
    c=0
    b=l.count(0)
    for 
    l.remove(0) 
    for i in range(b): 
        l.append(0)
    return l
    


x = [1, 0, 3, 0, 0, 5, 7] 
print(move(x))
x.append
y=move_zeros_v1(x)
print(x, y)

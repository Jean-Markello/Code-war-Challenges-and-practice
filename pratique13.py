"""Écrivez une fonction Python nommée qui va calculer le nombre d’occurrences 
d’une caractère c dans une chaine s. Essayez deux versions:
• avec la méthode count de la class str; et nommez votre fonction compteV1
• sans cette méthode (en utilisant une boucle while ou for) ; et nommez votre fonction 
compteV2
• Développez la partie principale du programme qui obtient de l’utilisateur une 
chaine de caractères nommé s, et appelle la fonction (les deux vesions) pour 
calculer le nombre de 'a'. La dernière partie doit être:"""


def compteV2(c,v):
    count=0
    for x in c:
        if x==v:
            count+=1
    return count

s="aaaskssksdjksaadjksd"
print(compteV2(s,'a'))
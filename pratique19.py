"""Question 3 :
a) Écrivez une fonction maListe(s, cible) qui prend une chaîne de mots s séparés par des espaces 
(en supposant qu'il n'y ait ni ponctuation ni majuscule), avec un mot « cible », et affiche la 
position du mot cible dans la chaîne de mots. Par exemple, si la chaîne est : 
je suis avec mon pere, mon ami et mon voisin
et la cible est le mot « mon » alors votre fonction devrait renvoyer la liste 3, 5, 8 car « mon » 
apparaît à la 3ème, 5ème et 8ème position dans la chaîne. (Nous commençons à compter les 
positions des mots dans la chaîne à partir de 0.) Votre fonction doit renvoyer False si le mot cible 
n'apparaît pas dans la chaîne. 
Exemple de deux exécutions :
>>> maListe("je suis avec mon pere, mon ami et mon voisin", "mon")
[3, 5, 8]
>>> maListe("je suis avec mon pere, mon ami et mon voisin", "ma")
False"""

def maListe(s,cible):
    count2=[]
    s=s.split(" ")
    if cible in s:
        for i in range(s.count(cible)):
            count2.append(s.index(cible))
            s[s.index(cible)]=2
        return count2
    else:
        return False
        



print(maListe("je suis avec mon pere mon ami et mon voisin", "mon"))
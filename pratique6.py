"""Écrivez une fonction appelée vote_percentage qui prend une chaîne en entrée. La fonction 
a un paramètre d'entrée, appelé résultat. Votre fonction doit compter le nombre de souschaînes « yes » dans résultat de la chaîne et le nombre de sous-chaînes « no » dans le 
résultat de la chaîne, et elle devrait renvoyer le pourcentage de « yes » (parmi tous « yes 
» et « no »). (Vous pouvez supposer que la chaîne résultat a au moins un yes ou un no et 
que les seuls mots présents sont yes, no et/ou abstained).
Astuce : vous pouvez utiliser la méthode count du module/bibliothèque str de Python."""

def vote_percentage(résuslat):
    
    c=résuslat.count("yes")
    b=résuslat.count("no")
    print(c,b)
    r=(c/(c+b))

    return r

s='abstained no abstained yes no yes no yes yes yes no'
print(vote_percentage(s))

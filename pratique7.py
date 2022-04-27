"""Question 7 :
S'il y a un vote lors d'une réunion, il y a plusieurs résultats possibles en fonction du 
nombre de votes oui et non (abstention ne sont pas comptés). Si tous les votes sont oui, 
alors la proposition passe "à l'unanimité", si au moins 2/3 des votes sont oui, alors la 
proposition passe avec "super majorité", si au moins 1/2 des voix sont oui, alors la 
proposition passe par "simple majorité", et sinon cela échoue. Écrivez une fonction 
nommée vote qui demande à un utilisateur d'entrer tous les oui-s et non-s et abstenu-s, 
puis appuyez sur Entrée. La fonction imprime alors le résultat du vote. Votre solution doit 
impliquer de faire un appel à fonction vote_percentage de la Question 6 (Vous pouvez 
supposer que l'utilisateur entrera au moins un oui ou un non et que les seuls mots 
présents sont oui, non et/ou abstenus)."""

def vote_percentage(résultat):
    c=résultat.count("yes")
    b=résultat.count("no")
    for x in résultat:
        if x!="yes" or x!="no":
            résultat.remove(x) 
    l=len(résultat)
    print(l)
    print(résultat)
    print(c/l)
    print(c,b)
    if c==l:
        print(1)
    elif c/l>0.67 and c/l<l:
        print(2)
    elif c/l==0.5:
        print(3)
    elif c/l<0.5:
        print(4) 


r=input("Entrer yes, no, abstain votes un par un et appuyer sur entrer:")
r=r.split(",")
print(r)
vote_percentage(r) 
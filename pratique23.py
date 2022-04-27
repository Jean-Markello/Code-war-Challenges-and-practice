def liste_longueurs_chaines(L):
    list=[]
    for x in L:
        list.append(len(x))
    return list
 

print(liste_longueurs_chaines(['un', 'deux', 'trois', 'quatre']))


def liste_carres(x):
    list=[]
    for v in x:
        list.append(v**2)
    return list

print(liste_carres([1, 2, 3, 4, 5]))
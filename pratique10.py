def somme_de_trois(x):
    somme=0
    l=len(x)-2
    for i in range(l):
        somme=x[i]+x[i+1]+x[i+2]
        if somme ==0:
            return True
    return False
        




t = (1,2,0,4,-1,3,4,5,6,7,8,0,5,-5)
print(somme_de_trois(t))

'''(tuple)->bool
Retourne True si la somme de 3 elements
consecutives est zero
Precondition: le tuple a au moins 3
elements
>>> t = (1,2,-3,4,-1,3)
>>> somme_de_trois(t)
True
'''


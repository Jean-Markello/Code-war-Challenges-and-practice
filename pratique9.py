
"""def histo_n(x):
    dic={}
    for c in x:
        dic[c]=dic.get(c,0)+1
    print(dic)
    return dic

t = tuple(eval(input("Elements: ")))
b=(histo_n(t))
b=list(b.items())
b.sort()
print(b)
"""
"""
def somme_de_trois(x):
    i=0
    while i<len(x)-2:
        if x[i]+x[i+1]+x[i+2]==0:
            return True
        i+=1
    return False

t = tuple(eval(input("Elements: ")))
print(somme_de_trois(t)) """


"""
def move_zeros_v1(x):
    tmp =[0]*len(x)
    i=0
    for xi in x:
        if xi !=0:
            tmp[i]=xi
            i+=1
    return tmp
l=[1,0,3,0,0,5,7]
print(l,move_zeros_v1(l))
"""

def move_zeros_v2(x):
    tmp =[0]*len(x)
    i=0
    for xi in x:
        if xi !=0:
            tmp[i]=xi
            i+=1
    for i in range(len(x)):
        x[i]=tmp[i]
l=[1,0,3,0,0,5,7]
z=move_zeros_v2(l)
print(l,z)


"""
def move_zeros_v3(x):
    f=0
    nzero=0
    while f+nzero<len(x):
        if x[f]==0:
            nzero+=1
            for i in range(f,len(x)-1):
                x[i]=x[i+1]
            x[-1]=0
        else:
            f+=1

l=[1,0,3,0,0,5,7]
z=move_zeros_v3(l)
print(l,z) """
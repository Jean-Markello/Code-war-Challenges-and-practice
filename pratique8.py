def fusionne(l,j):
    a=l+j
    for n in a:
        z=a.count(n)
        if z>1:
            a.remove(n)
    a.sort()
    return a
	
l,b=[1,2,8],[2,3,10,12]
print(fusionne(l,b)) 


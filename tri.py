
def tri_par_insertion(L):
    L2 = []
    i = 0
    while i != len(L):
        insert(L2, L[i])
        i = i + 1
    return L2

def insert(L, val):
    i = len(L)
    while i != 0 and L[i - 1] >= val:
        i = i - 1
    L.insert(i, val)


L = [3, 4, 7, -1, 2, 5]
print(tri_par_insertion(L))


"""Question 2 :
Écrire une fonction Python appelée ma_Fonction qui prend en entrée un entier, n où n est 
égal à 1 ou n est un entier positif. Votre fonction ne sera testée qu'avec de tels entiers n.
Si n vaut 1, la fonction doit demander à l'utilisateur un entier positif. La fonction doit 
afficher tous les diviseurs de l’entier rentré et retourner True si la donnée l'entier positif est 
pair et False sinon. (Vous pouvez supposer que l'utilisateur suivra les instructions et saisira 
un entier positif)
Sinon (n n’est pas égal à 1), la fonction doit renvoyer n. 
Exemple de deux exécutions :
>>> print(ma_Fonction(1))
Entrer un entier positif: 12
1
2
3
4
6
12
True
>>> print(ma_Fonction(1))
Entrer un entier positif: 3
1
3
False
>>> print(ma_Fonction(123))
123"""
def ma_Fonction(x):
    for i in range(1,x+1):
        if (x%i)==0:
            print(i)
    if x%2==0:
        return True
    else:
        return False

while True:
    b=int(input("Entrer un entier: "))
    if b!=1:
        break

print(ma_Fonction(b))
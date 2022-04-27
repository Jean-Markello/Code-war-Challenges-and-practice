"""Écrivez une fonction evalue_poly qui évalue les polynômes. Elle devrait prendre deux 
arguments evalue_poly(x, coeffs). Le premier est un nombre x. Le second est une liste de 
coefficients classés du plus élevé au plus bas :
Votre fonction doit retourner la valeur du polynôme évalué à x :
Exemple de deux exécutions :
>>>evalue_poly(1, [1,2,3])
6
>>>evalue_poly(2, [1,2,3,4])
26
"""
def evalue_poly(x, coeffs):
    total=0 #gardera un total cumulé de la somme 
    coeffs.reverse() # donner la priorité aux coefficients d'ordre inférieur 
    for i in range(len(coeffs)):
        total+=coeffs[i]*(x**i) #ajouter le terme courant au total 
    return total

print(evalue_poly(2, [1,2,3,4]))
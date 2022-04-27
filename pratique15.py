"""Écrivez une fonction Python nommée coder qui prend une chaine de caractères s 
et retourne une autre chaine codée. Le code est calculé par prendre chaque paire de 
lettres consécutives en échangeant l’ordre dans la paire (espaces, ponctuation, etc. 
sont traités comme les lettres).
• Testez votre fonction avec un programme principal, ou dans l’interpréteur. Par 
exemple:
>>> codez('message secret')
'emssga eesrcte'
>>> coder('Message')
‘eMssgae'"""

def coder(a):
    s=""
    for i in range(0,len(a),2):
        s+=a[i+1] + a[i]
        
    return s

msg='message secret'
print(coder(msg))
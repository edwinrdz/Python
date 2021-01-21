"""Encontrar la cantidad máxima de caracteres en orden alphabetical dentro de un String introducido"""
#97-122=26 letras


S=input('Ingrese su texto: ')
S=S.lower()
t=len(S)
Sb=S[0]

for i in range(t):
	if(i>0):
		if ord(S[i])>ord(S[i-1]):
			Sb=Sb+S[i]
		else:
			break

print(Sb)
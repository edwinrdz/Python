"""Crear una piramide de números apartir del valor maximo ingresado"""

n=int(input('Ingrese un numero: '))


for i in range(n):
	i+=1
	s=str(i)*i
	print(s)
	
for i in range(n):
	i=n-(i+1)
	s=str(i)*i
	print(s)
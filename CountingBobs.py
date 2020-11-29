#Programa para contar las veces que se repite la palabra bob

def counting_bobs(Texto):
	Texto2=Texto.lower()
	veces=0
	for i in range(len(Texto2)):
		if Texto2[i:i+3].count('bob')==1:
			veces += 1

	return f'there are {veces} bob´s'

Text=input('Escribe tu oracion: ')
numero_bobs=counting_bobs(Text)
print('\nEl texto introducido es: {}'.format(Text))
print(numero_bobs)



 
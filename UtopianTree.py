#Utopian Tree
"""El programa calcula la altura que alcanzaran cierta cantidad de arboles
1 CICLO->doble de la altura
2 CICLO2->+1m
altura inicial=1m.
"""
h=1
T=input('How many trees do you want to test?')
c=int(input('How many cycles for the tree do you want test?'))

for i in range(c):
	if (i+1)%2==0:
		h+=1
	else:
		h=h*2

print(f'The tree height of the {T} trees will be of {h} meters after {c} cycles')





import math

def prob_10(tupla1, tupla2, tupla3):
	d1= math.sqrt (((tupla2(0) - tupla1(0))**2 + (tupla2(1) - tupla1(1))**2))
	d2= math.sqrt (((tupla3(0) - tupla2(0))**2 + (tupla3(1) - tupla2(1))**2))
	d3= math.sqrt (((tupla1(0) - tupla3(0))**2 + (tupla1(1) - tupla3(1))**2))

	if d1 == d2 and d2 == d3:
		respuesta= ("Es un traingulo equilatero.")

	elif d1 == d2 and d2 != d3:
		respuesta= ("Es un triangulo isoceles.")

	elif d1 == d3 and d2 != d1:
		respuesta= ("Es un triangulo isoceles.")
		
	elif d2 == d3 and d3 != d1:
		respuesta= ("Es un triangulo isoceles.")			

	elif d1 != d2 and d2 != d3 and d1 != d3:
		respuesta= ("Es un triangulo escaleno.")	

	return respuesta	
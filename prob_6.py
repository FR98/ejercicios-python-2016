def prob_6 (lista):
	for a in range (len(lista)-1, 0, -1):
		for b in xrange (a):
			if lista[b] < lista[b+1]:
				lista[b], lista[b+1]= lista[b+1], lista[b]
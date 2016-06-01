def prob_11 (frase):
	sinEspacios = list(frase)
	fraseUnida = sinEspacios.join(sinEspacios)
	if frase == (nuevaFrase.reverse(fraseUnida)):
		return "Si es palindromo"
	else:
		return "No es palindromo"
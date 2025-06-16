def produtos_esgotados(j):
	for keys, values in j.items():
		if values == ' ' or all(v == 0 for v in values): # essa é a correção pelo chatgpt a partir do 'all'
		#if values == ' ' or values == 0: essa é a minha solução que deu erro
		    print (keys) 
			

#início do algoritmo
estoque_produtos = {'Arroz': [], 'Macarrão': [8.99, 10.20, 10]}

produtos_esgotados(estoque_produtos)
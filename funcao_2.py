def prod_disponiveis(b): 
    if b in estoque_produtos:
        disponib_prod = len(estoque_produtos[disponibilidade])
        return print (f'O produto solicitado apresenta {disponib_prod} disponíveis em estoque.')
    else:
        return print ('O produto não existe no estoque. Cadastro não encontrado.')

#início do algoritmo

estoque_produtos = {'Macarrão': [4.99, 5.89], 'Miojo': [0.99]}

disponibilidade = input ('Deseja verificar a disponibilidade de qual produto? ').title
            
prod_disponiveis(disponibilidade)
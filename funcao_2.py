def prod_disponiveis(b): 
    if disponibilidade in estoque_produtos:
        disponib_prod = len(estoque_produtos[disponibilidade])
        return print (f'O produto solicitado apresenta {disponib_prod} disponíveis em estoque.')
    else:
        return print ('O produto não existe no estoque. Cadastro não encontrado.')

#início do algoritmo

estoque_produtos = {'macarrão': [4.99, 5.89]}

disponibilidade = input ('Deseja verificar a disponibilidade de qual produto? ').title
            
prod_disponiveis(disponibilidade)
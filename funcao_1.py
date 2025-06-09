

def cadastro_prod(a):
    if a in (estoque_produtos):
        quantidade = int (input ('Quantos desse produto você quer cadastrar? '))
        for i in range(quantidade):
            preco = float (input ('Valor do produto: R$ '))
            estoque_produtos[a].append(preco)
    else:
        estoque_produtos[a] = []
        print ('Novo produto sendo cadastrado!')
        quantidade = int(input ('Quantos desse produto você quer cadastrar? '))
        for i in range(quantidade):
            preco = float (input ('Valor do produto: R$ '))
            estoque_produtos[a].append(preco)
    return print ('Produto cadastrado com sucesso!.')


#início do algoritmo

estoque_produtos = {}

produto = input ('Deseja cadastrar qual produto? ')

cadastro_prod(produto)
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

def prod_disponiveis(b): 
    if disponibilidade in estoque_produtos:
        disponib_prod = len(estoque_produtos[disponibilidade])
        return print (f'O produto solicitado apresenta {disponib_prod} unidades disponíveis em estoque.')
    else:
        return print ('O produto não existe no estoque. Cadastro não encontrado.')

def registro_vendas(c, d):
    if d in estoque_produtos[c]: #função com erro
        estoque_produtos[c] = ' '
        return print ('Um item  com esse valor foi eliminado do estoque. Venda feita!')
    else: 
        return print (f'Não existe um produto {c} com esse valor no estoque. ')

def relatorios(e):
    return print (f'----RELATóRIO DE ESTOQUE ----\n{e}\n ----FIM DO RELATóRIO----')

def quantidade_total_estoque(i):
    for keys, lista in i.items():
        quantidade_itens = len(lista)
        print (keys, quantidade_itens)

def produtos_esgotados(j):
	for keys, values in j.items():
		if values == ' ' or all(v == 0 for v in values): # essa é a correção pelo chatgpt a partir do 'all'
		#if values == ' ' or values == 0: essa é a minha solução que deu erro
		    print (keys) 

def total_vendas_produto(k,l,m):
    produto = k.get(m)
    valor = l
    return print (f'O valor total da venda do produto {produto} é R$ {valor}.') #esta imprimindo errado na variável produto, esta imprimindo o valor e não a chave
    
def faturamento_total(n): #não esta funcionando porque o registro de venda não esta funcionando
    print (f'O faturamento total é de R$ {n:.2f}.')

#main
estoque_produtos = {'Arroz':[5.50], 'Macarrão':[]}
soma_venda = 0
continuar = 'S'
total_estoque = 0
dict_vendas = {} #para ser usado na função 7

while True:
    print ('''
____ SISTEMA DE GESTÃO DE ESTOQUE E VENDAS ___

  1 - Cadastro de produtos com nome, preço e quantidade em estoque.
  2 - Consulta de produtos disponíveis.
  3 - Registro de vendas, com atualização automática do estoque.
  4 - Relatórios.
  5 - Produtos em estoque.
  6 - Produtos esgotados.
  7 - Total de vendas por produto.
  8 - Faturamento total.
  9 - Sair. 
''')

    try:
        opcao = int (input('Qual opção você escolhe? '))
    except ValueError:
        print (ValueError)

    match opcao:
        case 1:
            produto = input ('Deseja cadastrar qual produto? ').title()

            cadastro_prod(produto)
        
        case 2:
            disponibilidade = input ('Deseja verificar a disponibilidade de qual produto? ').title()
            
            prod_disponiveis(disponibilidade)

            # if disponibilidade in estoque_produtos:
            #     disponib_prod = len(estoque_produtos[disponibilidade])
            #     print (f'O produto solicitado apresenta {disponib_prod} disponíveis em estoque.')
            # else:
            
            #     print ('O produto não existe no estoque. Cadastro não encontrado.')
        case 3:
           while continuar == 'S':
                venda = input('De qual produto esta fazendo a venda? ').title()
                if venda not in estoque_produtos:
                    print ('O produto não se encontra em estoque.')
                    continue 

                try:
                    valor_venda = float (input('Valor da venda desse produto: R$ '))
                except:
                    print ('Valor inválido ou produto com estoque zerado!')
                
                continuar = input ('Quer fazer uma venda (S/N)? ').upper()
                
                registro_vendas(venda, valor_venda)

        case 4:
            relatorios(estoque_produtos)

        case 5:
            quantidade_total_estoque(estoque_produtos)

        case 6:
            produtos_esgotados(estoque_produtos)

        case 7:
            venda = input('De qual produto esta fazendo a venda? ')

            try:
                valor_venda = float (input('Valor da venda desse produto: R$ '))
            except:
                print ('Valor inválido!')

            dict_vendas[venda] = []

            if venda in dict_vendas:
                dict_vendas[venda].append(valor_venda)
                soma_venda = valor_venda #para ser usado também na função 8
            else:
                dict_vendas.update({venda:valor_venda})

            total_vendas_produto(dict_vendas, soma_venda, venda)

        case 8:
            while continuar == 'S':
                venda = input('De qual produto esta fazendo a venda? ').title()
                if venda not in estoque_produtos:
                    print ('O produto não se encontra em estoque.')
                    continue 

                try:
                    valor_venda = float (input('Valor da venda desse produto: R$ '))
                except:
                    print ('Valor inválido ou produto com estoque zerado!')

                dict_vendas[venda] = []

                #if venda in dict_vendas:
                dict_vendas[venda].append(valor_venda)
                
                soma_venda += valor_venda #para ser usado também na função 8
                #else:
                #   dict_vendas.update({venda:valor_venda})

                continuar = input ('Quer fazer uma venda (S/N)? ').upper()

                faturamento_total(soma_venda)
        case 9:
            break
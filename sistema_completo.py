
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

    estoque_produtos = {}

    match opcao:
        case 1:
            produto = input ('deseja cadastrar qual produto? ')

            cadastro_prod(produto)
        

        case 2:
            disponibilidade = input ('Deseja verificar a disponibilidade de qual produto? ')
            
            prod_disponiveis(disponibilidade)

            if disponibilidade in estoque_produtos:
                disponib_prod = len(estoque_produtos[disponibilidade])
                print (f'O produto solicitado apresenta {disponib_prod} disponíveis em estoque.')
            else:
                print ('O produto não existe no estoque. Cadastro não encontrado.')
        case 3:
            venda = input('De qual produto esta fazendo a venda? ')
            try:
                valor_venda = float (input('Valor da venda desse produto: R$ '))
            except:
                print ('Valor inválido!')

            registro_vendas(venda, valor_venda)

        case 4:
            relatorios()
        case 5:
            quantidade_total_estoque ()
            quantidade_total_estoque = estoque_produtos[a].append(preco)
            prod_estoque()
        case 6:
            total_vendas()
        case 7:
            total_faturamento()
        case 8:
            break


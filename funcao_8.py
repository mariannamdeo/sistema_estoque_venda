def faturamento_total(n):
    print (f'O faturamento total é de R$ {n:.2f}.')

#main
estoque_produtos = {'Macarrão': [8.99, 10.20, 10],'Arroz': [5, 7, 9.99]}
soma_venda = 0
continuar = 'S'
dict_vendas = {} #para ser usado na função 7

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
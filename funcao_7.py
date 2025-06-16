def total_vendas_produto(k,l,m):
    produto = k.get(m)
    valor = l
    return print (f'O valor total da venda do produto {produto} é R$ {valor}.') #esta imprimindo errado na variável produto, esta imprimindo o valor e não a chave
    


#main
estoque_produtos = {'Macarrão': [8.99, 10.20, 10],'Arroz': [5, 7, 9.99]}

venda = input('De qual produto esta fazendo a venda? ')

try:
    valor_venda = float (input('Valor da venda desse produto: R$ '))
except:
    print ('Valor inválido!')

dict_vendas = {} #para ser usado na função 7
soma_venda = 0
dict_vendas[venda] = []

if venda in dict_vendas:
    dict_vendas[venda].append(valor_venda)
    soma_venda = valor_venda #para ser usado também na função 8
else:
     dict_vendas.update({venda:valor_venda})

total_vendas_produto(dict_vendas, soma_venda, venda)
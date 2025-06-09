def registro_vendas(c, d):
    if d in registro_vendas[c]:
        estoque_produtos[c] = ''
        print ('Um item  com esse valor foi eliminado do estoque. Venda feita!')
    else: 
        print (f'Não existe um produto {c} com esse valor no estoque. ')

   

#início do algoritmo

estoque_produtos = {'Macarrão': [8.99, 10.20, 10]}

venda = input('De qual produto esta fazendo a venda? ')
try:
    valor_venda = float (input('Valor da venda desse produto: R$ '))
except:
    print ('Valor inválido!')

registro_vendas(venda, valor_venda)
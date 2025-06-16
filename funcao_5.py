def quantidade_total_estoque(i):
    for keys, lista in i.items():
        quantidade_itens = len(lista)
        print (keys, quantidade_itens)

#início do algoritmo
estoque_produtos = {'Macarrão': [8.99, 10.20, 10],'Arroz': [5, 7, 9.99]}
#total_estoque = 0

#contador_frequencia = {}

quantidade_total_estoque(estoque_produtos)
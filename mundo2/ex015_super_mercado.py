print('-=-'*20)
print('SUPER BARATÃO')
print('-=-'*20)
totalgasto = 0
contador = 0
produto_caro = 0
menor_preco = 0
nome_mais_barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$'))
    totalgasto += preco
    contador += 1
    if preco >= 1000:
        produto_caro += 1
    if contador == 1:
        menor_preco = preco
        nome_mais_barato = produto
    elif preco < menor_preco:
        menor_preco = preco
        nome_mais_barato = produto
    continuar = ' '
    while continuar not in 'SN':
       continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('---------- FIM DO PROGRAMA ----------')
print(f'O total gasto na compra foi de R${totalgasto}')
print(f'Temos {produto_caro} produto(s) custando mais de R$1000')
print(f'O produto mais barato foi {nome_mais_barato} que custa R${menor_preco}')

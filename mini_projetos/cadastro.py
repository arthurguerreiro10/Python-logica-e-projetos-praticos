print('-=-'*15)
print('CADASTRE UMA PESSOA')
print('-=-'*15)
homens = 0
mulherestotais = 0
mulheres = 0
maioridade = 0
while True:
    idade = int(input('Idade: '))
    continuar = ' '
    escolha = ' '
    if idade >= 18:
        maioridade += 1
    while escolha not in 'MF':
       escolha = str(input('Sexo [M/F]: ')).strip().upper()[0]
       if escolha == 'F' and idade < 20:
           mulherestotais += 1
       if escolha == 'M':
           homens += 1
       elif escolha == 'F':
           mulheres += 1
    while continuar not in 'SN':
       print('-=-'*20)
       continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
       print('-=-'*20)
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulherestotais} mulheres com menos de 20 anos')

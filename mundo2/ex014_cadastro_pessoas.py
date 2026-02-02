maior_idade = 0
homens = 0
mulheres_menos_20 = 0

while True:
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]

    if idade >= 18:
        maior_idade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break

print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menos_20} mulheres com menos de 20 anos')

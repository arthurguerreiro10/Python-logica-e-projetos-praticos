nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'Média do aluno: {media}')

if media >= 6:
    print('Aluno APROVADO')
else:
    print('Aluno REPROVADO')

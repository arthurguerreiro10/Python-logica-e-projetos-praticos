print('-=-'*15)
print('BANCO GUERREIRO')
print('-=-'*15)
valor = int(input('Que valor você quer sacar?: '))
cedula = 50
contador = 0
while valor > 0:
    if valor >= cedula:
        valor -= cedula
        contador += 1
    elif valor < cedula:
        if cedula == 50:
            print(f'Total de {contador} cédulas de R${cedula}')
            cedula = 20
            contador = 0
        elif cedula == 20:
            print(f'Total de {contador} cédulas de R${cedula}')
            cedula = 10
            contador = 0
        elif cedula == 10:
            print (f'Total de {contador} cédulas de R${cedula}')
            cedula = 1
            contador = 0
if contador > 0:
    print(f'Total de {contador} cédulas de R${cedula}')
print('-=-'*15)
print('Volte sempre ao BANCO GUERREIRO! Tenha um bom dia.')

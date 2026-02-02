while True:
    numero = int(input('Quer ver a tabuada de qual valor?: '))
    if numero < 0:
       break
    print('--' *20)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')
    print('--'*20)
  
print('--'*20)
print('Programa de tabuada encerrado! Volte sempre.')

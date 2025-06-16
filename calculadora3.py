print ('calculadora no python')
print ('escolha a sua opçao')
print ('[1] Adição')
print ('[2] subtração')
print ('[3] multiplicação')
print ('[4] divisão')

opçao = int(input())

numero1 = int(input('digite o primeiro numero'))
numero2 = int(input('digite o segundo numero'))

if opçao == 1:
    print(f'o resultado da soma: {numero1 + numero2}')
elif opçao == 2:
    print(f'o resultado da subtraçao: {numero1 - numero2}')
elif opçao == 3:
    print(f'o resultado da multipçica: {numero1 * numero2}')
elif opçao == 4:
    print(f'o resultado da divisao: {numero1 / numero2}')

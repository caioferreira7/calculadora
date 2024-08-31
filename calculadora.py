#Calculadora_Simples

calcular = input('''
Insira os sinais matemáticos para as devidas operações:
+ adição
- subtração
* multiplicação
/ divisão
''')

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))

if calcular == '+':
    print('{} + {}' .format(num1,num2))
    print(num1 + num2)

elif calcular == '-':
    print('{} - {}'.format(num1,num2))
    print(num1 - num2)

elif calcular == '*':
    print('{} * {}' .format(num1,num2))
    print(num1 * num2)

elif calcular == '/':
    print('{} / {}' .format(num1,num2))
    print(num1 / num2)

else:
    print('Você digitou um operador não válido, refaça.')


calcular2 = input('''
Você quer calcular de novo?
Digite S para SIM ou N para não.
''')

if calcular2 == 'S':
    calcular

elif calcular2 == 'N':
    print('Até outra hora.')

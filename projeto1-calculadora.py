import os


def menu():
    print('CALCULADORA ASIMOV')
    print('1 para soma (+)')
    print('2 para substração (-)')
    print('3 para multiplicação (x)')
    print('4 para divisão (/)')
    print('0 para SAIR')
    print()  # linha em branco para melhor visualização

    opcao = int(input('Informe a opção desejada: '))
    while opcao not in [0, 1, 2, 3, 4]:
        print('Opção inválida!')
        opcao = int(input('Informe a opção desejada: '))
    return opcao

def limpar_console():
    os.system('cls')

def somar(n1, n2):
    resultado = num1 + num2
    print('\nResultado: {} + {} = {}\n'.format(n1, n2, resultado))

def subtrair(n1, n2):
    resultado = num1 - num2
    print('\nResultado: {} - {} = {}\n'.format(n1, n2, resultado))

def multiplicar(n1, n2):
    resultado = num1 * num2
    print('\nResultado: {} * {} = {}\n'.format(n1, n2, resultado))

def dividir(n1, n2):
    resultado = num1 / num2
    print('\nResultado: {} / {} = {}\n'.format(n1, n2, resultado))


while True:
    limpar_console()
    escolha = menu()

    if escolha == 0:
        print('Encerrando...')
        break

    num1 = float(input('\nInforme o primeiro número: '))
    num2 = float(input('\nInforme o segundo número: '))

    if escolha == 1:
        somar(num1, num2)
    elif escolha == 2:
        subtrair(num1, num2)
    elif escolha == 3:
        multiplicar(num1, num2)
    elif escolha == 4:
        dividir(num1, num2)
    else:
        print('Encerrando...')
        break

    input('Pressione ENTER para continuar...')  # Pausa antes de limpar
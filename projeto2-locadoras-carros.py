import os

OPCAO_INVALIDA = 'Opção inválida!'

def limpar_console():
    os.system('cls')

def menu_principal():
    limpar_console()
    print('LOCADORA ASIMOV')
    print('Escolha a opção desejada')
    print('1 - Portfolio')
    print('2 - Alugar carro')
    print('3 - Devolver carro')
    print('0 - Sair')
    resposta = input('Informe a opção desejada: ')

    while resposta not in ['0', '1', '2', '3']:
        print('Opção inválida')
        resposta = input('Informe a opção desejada: ')

    return int(resposta)

def exibir_portfolio():
    limpar_console()
    print('PORTIFÓLIO')
    exibir_carros()

def alugar_carro():
    limpar_console()
    print('ALUGAR CARRO')

    if all(carro['alugado'] for carro in carros):
        print('Não há carros disponíveis para aluguel.')
        return

    exibir_carros(False)

    carro_informado = input('\nInforme o carro a ser alugado: ')

    while not carro_informado.isnumeric() or int(carro_informado) > len(carros) or int(carro_informado) < 1 or \
            carros[int(carro_informado) - 1]['alugado'] is True:
        print(OPCAO_INVALIDA)
        carro_informado = input('Informe o carro a ser alugado: ')

    dias = input('\nInforme a quantidade de dias: ')

    while not dias.isnumeric() or int(dias) < 1 :
        print(OPCAO_INVALIDA)
        dias = input('Informe a quantidade de dias: ')

    print('\nVocê selecionou {} por {} {} de aluguuel. Total: R$ {}.'.format(carros[int(carro_informado) - 1]['modelo'], int(dias), 'dias' if int(dias) > 0 else 'dia', carros[int(carro_informado) - 1]['valor'] * int(dias)))

    carros[int(carro_informado) - 1]['alugado'] = True

def devolver_carro():
    limpar_console()
    print('DEVOLVER CARRO')

    if all(not carro['alugado'] for carro in carros):
        print('Não há carros alugados..')
        return

    exibir_carros(True)

    carro_informado = input('\nInforme o carro a ser devolvido: ')

    while not carro_informado.isnumeric() or int(carro_informado) > len(carros) or int(carro_informado) < 1 or \
    carros[int(carro_informado) - 1]['alugado'] is False:
        print(OPCAO_INVALIDA)
        carro_informado = input('Informe o carro a ser devolvido: ')

    carros[int(carro_informado) - 1]['alugado'] = False

def exibir_carros(filtro=None):
    for i in range(len(carros)):
        if filtro is None or carros[i]['alugado'] == filtro:
            print('[{}] {} - R$ {}/dia'.format(i+1, carros[i]['modelo'], carros[i]['valor']))

carros = [
    {
        'modelo': 'Chevrolet Tracker',
        'valor': 140,
        'alugado': False
    },
    {
        'modelo': 'Hiunday Creta',
        'valor': 160,
        'alugado': False
    },
    {
        'modelo': 'Jeep Compass',
        'valor': 180,
        'alugado': True
    },
    {
        'modelo': 'Nissan Kicks',
        'valor': 120,
        'alugado': False
    },
    {
        'modelo': 'Volkswagen Nivus',
        'valor': 100,
        'alugado': False
    },
    {
        'modelo': 'Renault Kardian',
        'valor': 80,
        'alugado': False
    },
]

while True:
    opcao = menu_principal()
    if opcao == 1:
        exibir_portfolio()
    elif opcao == 2:
        alugar_carro()
    elif opcao == 3:
        devolver_carro()
    else:
        break
    input('\n--- Aperte qualquer tecla para continuar ---')
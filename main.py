from os import system
from time import sleep
from Banco_de_Dados import layout, cadastros
from Banco_de_Dados.cadastros import cabeçalho
from Banco_de_Dados.cores import vermelho, negrito

# Programa principal
fim = False
while not fim:
    layout.layout()
    resposta = input(f'{negrito}Sua resposta: ')
    cabeçalho('Processando...')
    sleep(1)
    if resposta == '1':
        system('cls')
        cadastros.listar()
    elif resposta == '2':
        system('cls')
        cadastros.cadastrar()
    elif resposta == '3':
        system('cls')
        cabeçalho(f'Saindo...', vermelho)
        fim = True

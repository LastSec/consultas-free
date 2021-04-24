from os import system
from time import sleep
from subprocess import run
import requests
import re
import base64
import banner as b

# Cores
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;1m'


def tipos():
    print(f'''
{C}{G}•{C} Ferramentas: 
[{G}1{C}] CPF Completo.
[{G}2{C}] CEP BASICO.
[{G}3{C}] CEP AVANÇADO [moradores].
[{G}4{C}] TELEFONE [operadora].
[{G}5{C}] IP.
[{G}6{C}] Gerar CPF.
''')
    tool = input(f'{C}[{G}+{C}] Selecione uma Ferramenta DE ({G}1 {C}a {G}6{C}): ' + B)

    if tool == '1':
        cpf = input(f'{C}[{G}*{C}] Digite o CPF que deseja consultar: {B}')
        print()
        cpf = re.sub('[^0-9]+', '', cpf)
        consulta(cpf)

    elif tool == '6':
        gerarcpf()

    else:
        print(f'{C}[{R}-{C}] BASE INSTÁVEL 🙁.')

        sleep(1)
        tipos()


def gerarcpf():
    print(f'{C}[{G}*{C}] Gerando CPF...')

    sleep(1)
    cpf = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
    cpf2 = cpf['data']['number_formatted']
    cpf = cpf['data']['number']
    print(f'{C}[{Y}i{C}] O CPF gerado foi: {B} {cpf2}')

    sleep(1)
    print(f'{C}[{G}*{C}] Consultando CPF gerado...\n')
    consulta(cpf)


def consulta(cpf):
    print(f'{C}A base CONSULTA está se passando por manutenção, Acompanhem novas atualizações No Canal [LastSec] do YouTube.{C}\n')
    exit()


if __name__ == '__main__':
    system('clear')
    print(f'{G}Checando por atualizacoes... {C}')
    run(["git", "pull"])
    system('clear')
    print(b.banner)
    sleep(3)
    system('clear')
    print(b.banner2)
    tipos()


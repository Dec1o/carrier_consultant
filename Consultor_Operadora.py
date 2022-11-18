#Necessário baixar a biblioteca "phonenumbers", pip install phonenumbers

import phonenumbers
from phonenumbers import carrier

try:
    print('=' * 45)
    Nome = input('Digite o seu nome: ')
    telefone = input('Digite o número de telefone: ')

    print(f'\n{Nome}, a operadora deste número é: {(carrier.name_for_number(phonenumbers.parse(telefone), "en"))}')
    print('=' * 45)

except:
    print('Número ausente ou inválido, insira o número de telefone com o código do país:')

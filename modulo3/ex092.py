#Exercício 092 - Cadastro de trabalhador em Python
from datetime import datetime
cad = dict()
cad['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cad['idade'] = datetime.now().year - nasc
cad['ctps'] = int(input('Carteira de Trabalho (0 - não tem):'))

if cad['ctps'] != 0:
    cad['contratação'] = int(input('Ano de Contratação: '))
    cad['salário'] = float(input('Salário: R$'))
    cad['aposentadoria'] = cad['idade'] + ((cad['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in cad.items():
    print(f' - {k} é igual a: {v}')
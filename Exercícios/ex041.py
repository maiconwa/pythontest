"""Desafio 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade.
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
- Acima de 20 anos: MASTER"""

from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano = int(date.today().year)
idade = ano - nascimento
if idade <= 9:
    print('A categoria para este atleta que tem {} anos é a MIRIM.'.format(idade))
elif idade <= 14:
    print('A categoria para este atleta que tem {} anos é a INFANTIL.'.format(idade))
elif idade <= 19:
    print('A categoria para este atleta que tem {} anos é a JÚNIOR.'.format(idade))
elif idade <= 20:
    print('A categoria para este atleta que tem {} anos é a SÊNIOR'.format(idade))
else:
    print('A categoria para este atleta que tem {} anos é a MASTER'.format(idade))

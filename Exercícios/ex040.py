"""Desafio 040:
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('O aluno obteve a média {:.1f}. O aluno está REPROVADO.'.format(media))
elif 5.0 <= media <= 6.9:
    print('O aluno obteve a média {:.1f}. O aluno está de RECUPERAÇÃO.'.format(media))
elif media >= 7.0:
    print('O aluno está APROVADO com {:.1f} de média.'.format(media))

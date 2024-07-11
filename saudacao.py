'''
Faça um programa que peça a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada.
Ex. Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
'''

entrada = input('Por favor, digite a hora atual em números inteiros: ');

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!');
    elif hora <= 17:
        print('Boa tarde!');
    elif hora <=18:
        print('Boa noite!');
    else:
        print('Hora inválida.')
except:
    print('Entrada inválida.');

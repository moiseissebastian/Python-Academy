#Programa de teste para o Python no Zorin OS

time1 = str(input('Qual o nome do primeiro time? '));
time2 = str(input('Qual o nome do segundo time? '));

gols_time1 = input(f'Quantos gols o {time1} fez? ');
gols_time2 = input(f'Quantos gols o {time2} fez? ');

if gols_time1 > gols_time2:
    print(f'O {time1} venceu!');
elif gols_time2 > gols_time1:
    print(f'O {time2} venceu!');
else:
    print('O jogo empatou :(');

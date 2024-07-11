'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada.
'''

numero = input('Você deseja ver a tabuada de qual número? ')

numero_int = int(numero)
contador = 1
while contador <= 10:
    multiplicacao = numero_int * contador
    linha_tabuada = f'{numero_int} X {contador} = {multiplicacao}'
    print(linha_tabuada)
    contador += 1
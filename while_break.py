"""
Repetições
While(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
break = Para a execução do laço
continue = pula a execução do laço e retorna para o início
"""

condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    if nome.isdigit():
        print('Digite um nome com letras')
    else:
        print(f'Seu nome é {nome}')
        break
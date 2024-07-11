'''
Iterando strings com while
'''

nome = 'Moiseis Sebastian'  #Iterável

novo_nome = ''
contador = 0
while contador < len(nome):
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1

novo_nome += '*'
print(novo_nome)

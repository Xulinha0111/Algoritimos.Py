#------- Exercício 1 --------#
""" 
Autor: Julia Bellini Sorrente
Data: 02/09/2022 10:10 - 10:40

"Crie uma função que receba como parâmetro uma lista de cinco números 
inteiros preenchidos pelo usuário e que retorne a soma e a média desses valores."
"""

#Função Soma
def Soma(numeros):
    soma = sum(numeros)
    print(f'\nA SOMA é {soma}')

#Função Média
def Media(numeros1):
    media = sum(numeros1) / len(numeros1)
    print(f'\nA MÉDIA é {media}')

#Criação da Lista
lista = []

for i in range(5):
    lista.append(int(input('DIGITE UM NÚMERO: ')))

Soma(lista)
Media(lista)
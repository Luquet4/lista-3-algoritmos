from random import randint
from functools import reduce

'''
    - Exercicio 3
        Somar os números de uma lista (com reduce)
        Crie uma função que, utilizando reduce e uma função lambda, receba uma lista de
        números inteiros e retorne a soma total dos números.
        Exemplo de entrada: [1, 2, 3, 4]
        Exemplo de saída: 10
'''

numeros_aleatorios = [randint(-1000, 1000) for _ in range(10)]
soma = reduce(lambda x, y: x + y, numeros_aleatorios)

print(numeros_aleatorios)
print(soma)
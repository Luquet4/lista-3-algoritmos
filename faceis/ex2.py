from random import randint

'''
    - Exercicio 2
        Filtrar números pares de uma lista (com filter)
        Escreva uma função que, utilizando filter e uma função lambda, receba uma lista
        de números inteiros e retorne apenas os números pares.
        Exemplo de entrada: [1, 2, 3, 4, 5]
        Exemplo de saída: [2, 4]
'''

numeros_aleatorios = [randint(-1000, 1000) for _ in range(10)]
pares = list(filter(lambda x: x if x % 2 == 0 else None, numeros_aleatorios))

print(numeros_aleatorios)
print(pares)
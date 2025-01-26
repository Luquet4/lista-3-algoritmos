from random import randint

'''
    - Exercicio 1
        Dobrar elementos de uma lista
        Escreva uma função que, utilizando map e uma função lambda, receba uma lista
        de números inteiros e retorne uma nova lista com todos os elementos dobrados.
        Exemplo de entrada: [1, 2], Exemplo de saída: [2, 4, 6, 8]
'''

numeros_aleatorios = [randint(-1000, 1000) for _ in range(10)]
dobrar = list(map(lambda x: x * 2, numeros_aleatorios))

print(numeros_aleatorios)
print(dobrar)
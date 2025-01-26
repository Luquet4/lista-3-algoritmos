from random import randint

'''
    - Exercicio 5 
        5. Elevar números ao quadrado e ordenar (com map e sorted)
        Crie uma função que eleve ao quadrado todos os números de uma lista, utilizando
        map, e depois retorne a lista ordenada.
        Exemplo de entrada: [3, 1, 4, 2]
        Exemplo de saída: [1, 4, 9, 16]
'''

numeros_aleatorios = [randint(-1000, 1000) for _ in range(10)]

quadrado = sorted(list(map(lambda x: x * x, numeros_aleatorios)))

print(numeros_aleatorios)
print(quadrado)


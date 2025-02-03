from random import randint

'''
    - Exercicio 9
        Escreva uma função que receba uma lista de tuplas, onde cada tupla contém
        números inteiros. Utilize map e filter para filtrar as tuplas cuja média dos valores
        seja maior que 5.
        Exemplo de entrada: [(2, 8), (4, 5, 6), (1, 2)]
        Exemplo de saída: [(2, 8), (4, 5, 6)]
'''

tuple_list = [(randint(-100, 100), randint(-100, 100)) for _ in range(10)]

print(tuple_list)

out = list(filter(lambda x: x, map(lambda x: x if sum(x) / len(x) > 5 else None, tuple_list))) # Daria para fazer somente com um filter... mas como o enunciado pediu filter e map, então foi utilizado os dois.
print(out)
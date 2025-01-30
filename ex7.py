from random import randint

'''
    - Exercicio 7
        Agrupar números em categorias (com dicionários e lambdas)
        Escreva uma função que receba uma lista de números inteiros e utilize map e filter
        para criar um dicionário que agrupe os números em três categorias:
        o "positivos" (números maiores que 0)
        o "negativos" (números menores que 0)
        o "zeros" (números iguais a 0).
        o Exemplo de entrada: [1, -2, 0, 3, -5, 0]
        o Exemplo de saída: {"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}
'''

numeros_aleatorios = [randint(-1000, 1000) for _ in range(10)]

num_dict = {'positivos': [], 'negativos': [], 'zeros': []}

saida = list(filter(lambda x: num_dict['positivos'].append(x) if x > 0 else num_dict['negativos'].append(x) if x < 0 else num_dict['zeros'].append(x), numeros_aleatorios))

print(numeros_aleatorios)

print(num_dict)
from random import randint
from functools import reduce
'''
    Exercicio 10 - 
        Crie uma função que receba um dicionário onde as chaves são nomes de alunos e
        os valores são listas de notas (com pesos na última posição). A função deve calcular
        a média ponderada de cada aluno usando reduce e retornar um novo dicionário
        com os resultados.
        Exemplo de entrada:
        {
        "João": [8, 7, 9, 2], # (notas: 8, 7, 9; peso: 2)
        "Ana": [5, 6, 7, 3] # (notas: 5, 6, 7; peso: 3)
        }
        Exemplo de saída:
        {
        "João": 8.0,
        "Ana": 6.0
        }
'''

students_dict = {'João': [randint(0, 10) for _ in range(3)] + [2],
                 'Ana': [randint(0, 10) for _ in range(3)] + [3]
                 }
dict_out = {student: f"{reduce(lambda x, y: x + y * grades[-1], grades[:-1], 0) / sum([grades[-1]] * len(grades[:-1])):.2f}" for student, grades in students_dict.items()}

print(students_dict)
print(dict_out)
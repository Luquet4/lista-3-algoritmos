from functools import reduce

'''
    - Exercicio 8 
        Crie uma função que receba uma lista de palavras e retorne a soma total de letras
        em todas as palavras, utilizando map para contar as letras e reduce para somar.
        Exemplo de entrada: ["casa", "python", "lambda"]
        Exemplo de saída: 16
'''
names = ['casa', 'python', 'lambda', 'abcd']

out = reduce(lambda x,  y: x + y, list(map(lambda x: len(x), names)))

print(out)
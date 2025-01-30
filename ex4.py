'''
    - Exercicio 4
        Nomes com mais de 5 letras (com filter)
        Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne
        apenas os nomes com mais de 5 letras.
        Exemplo de entrada: ["Ana", "Lucas", "Fernanda", "João"]
        Exemplo de saída: ["Lucas", "Fernanda"]
'''

lista_nomes = ['Ana', 'Lucas', 'Fernanda', 'João']
nomes = list(filter(lambda x: x if len(x) >= 5 else None, lista_nomes))

print(nomes)
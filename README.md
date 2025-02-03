
# Exercícios de Manipulação de Listas e Dicionários em Python

Este repositório contém uma série de exercícios que utilizam funções como `map()`, `filter()`, `reduce()` e `lambda` para manipulação de listas e dicionários. Os exercícios estão organizados por níveis de dificuldade: **Fáceis**, **Médios** e **Difíceis**. 

## Estrutura do Repositório

- **Ex1.py**: Dobra todos os elementos de uma lista de números inteiros usando `map` e uma função `lambda`.
- **Ex2.py**: Filtra os números pares de uma lista de inteiros utilizando `filter` e uma função `lambda`.
- **Ex3.py**: Utiliza `reduce` e uma função `lambda` para somar todos os elementos de uma lista de números inteiros.
- **Ex4.py**: Filtra os nomes com mais de 5 letras de uma lista utilizando `filter` e uma função `lambda`.
- **Ex5.py**: Eleva ao quadrado todos os números de uma lista usando `map` e em seguida ordena a lista resultante.
- **Ex6.py**: Cria um dicionário com números pares e ímpares a partir de uma lista de números inteiros utilizando `lambda` e `filter`.
- **Ex7.py**: Agrupa números em três categorias: "positivos", "negativos" e "zeros", utilizando `map` e `filter`.
- **Ex8.py**: Conta o número total de letras em uma lista de palavras utilizando `map` para contar as letras e `reduce` para somar.
- **Ex9.py**: Filtra as tuplas de uma lista cuja média dos valores seja maior que 5 utilizando `map` e `filter`.
- **Ex10.py**: Calcula a média ponderada dos alunos utilizando `reduce` e `lambda` com um dicionário de notas e pesos.

## Como Executar os Exercícios

1. Clone o repositório ou baixe os arquivos.
2. Para cada exercício, basta executar o arquivo correspondente, por exemplo:
   ```bash
   python Ex1.py
   ```
3. Cada arquivo realiza a operação descrita e imprime os resultados no console.

## Exemplo de Uso

Aqui estão alguns exemplos de saída de cada exercício, baseados nas operações implementadas:

- **Ex1.py**:  
  **Entrada:** `[1, 2, 3, 4]`  
  **Saída:** `[2, 4, 6, 8]`

- **Ex2.py**:  
  **Entrada:** `[1, 2, 3, 4, 5]`  
  **Saída:** `[2, 4]`

- **Ex3.py**:  
  **Entrada:** `[1, 2, 3, 4]`  
  **Saída:** `10`

- **Ex4.py**:  
  **Entrada:** `["Ana", "Lucas", "Fernanda", "João"]`  
  **Saída:** `["Lucas", "Fernanda"]`

- **Ex5.py**:  
  **Entrada:** `[3, 1, 4, 2]`  
  **Saída:** `[1, 4, 9, 16]`

- **Ex6.py**:  
  **Entrada:** `[1, 2, 3, 4, 5, 6]`  
  **Saída:** `{"pares": [2, 4, 6], "ímpares": [1, 3, 5]}`

- **Ex7.py**:  
  **Entrada:** `[1, -2, 0, 3, -5, 0]`  
  **Saída:** `{"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}`

- **Ex8.py**:  
  **Entrada:** `["casa", "python", "lambda"]`  
  **Saída:** `16`

- **Ex9.py**:  
  **Entrada:** `[(2, 8), (4, 5, 6), (1, 2)]`  
  **Saída:** `[(2, 8), (4, 5, 6)]`

- **Ex10.py**:  
  **Entrada:**  
  ```python
  {"João": [8, 7, 9, 2], "Ana": [5, 6, 7, 3]}
  ```  
  **Saída:**  
  ```python
  {"João": 8.0, "Ana": 6.0}
  ```

# Implementação do Selection Sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Encontra o índice do menor elemento na sublista restante
        indice_menor = i
        for j in range(i + 1, n):
            if lista[j]['pontuacao'] < lista[indice_menor]['pontuacao']:
                indice_menor = j
        # Troca o elemento atual com o menor encontrado
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

# Exemplo de uso
jogadores = [
    {"nome": "João", "pontuacao": 50},
    {"nome": "Ana", "pontuacao": 30},
    {"nome": "Carlos", "pontuacao": 40},
    {"nome": "Beatriz", "pontuacao": 20}
]

selection_sort(jogadores)
print(jogadores)

# O Selection Sort funciona assim:
# 1. Para cada posição da lista (i), ele encontra o menor elemento na sublista restante.
# 2. Troca o menor elemento encontrado com o elemento na posição atual (i).
# 3. Repete até que toda a lista esteja ordenada.
# A complexidade do Selection Sort é O(n^2), porque há dois laços aninhados: 
# o primeiro percorre os elementos da lista e o segundo busca o menor elemento na sublista.
# Apesar de ser simples, ele é menos eficiente para listas grandes comparado a algoritmos mais avançados.
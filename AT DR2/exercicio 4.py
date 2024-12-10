def busca_binaria(lista, isbn_procurado):
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if lista[meio]['isbn'] == isbn_procurado:
            return lista[meio], iteracoes
        elif lista[meio]['isbn'] < isbn_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return "ISBN não encontrado", iteracoes

def busca_linear(lista, isbn_procurado):
    iteracoes = 0
    for livro in lista:
        iteracoes += 1
        if livro['isbn'] == isbn_procurado:
            return livro, iteracoes
    return "ISBN não encontrado", iteracoes

# Exemplo prático, poderia ser 100 mil livros
livros = [
    {"titulo": "Livro A", "isbn": 123},
    {"titulo": "Livro B", "isbn": 456},
    {"titulo": "Livro C", "isbn": 789}
]

isbn = 456

# Busca binária
resultado_binaria, iteracoes_binaria = busca_binaria(livros, isbn)
print(f"Busca Binária: {resultado_binaria}, Iterações: {iteracoes_binaria}")

# Busca linear
resultado_linear, iteracoes_linear = busca_linear(livros, isbn)
print(f"Busca Linear: {resultado_linear}, Iterações: {iteracoes_linear}")

# O algoritmo de busca binária divide a lista pela metade a cada iteração, fazendo com que
# o número de iterações cresça de forma logarítmica (O(log n)). Já a busca linear percorre
# todos os elementos até encontrar o ISBN, com número de iterações proporcional ao tamanho da lista (O(n)).
# A busca binária é muito mais eficiente em listas grandes, como a de 100 mil livros.

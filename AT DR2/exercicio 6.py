import time

# Implementação do Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Função para medir o tempo de execução
def testar_bubble_sort(tamanho):
    from random import randint
    lista = [randint(1, 1000) for _ in range(tamanho)]
    inicio = time.time()
    bubble_sort(lista)
    fim = time.time()
    return fim - inicio

# Teste com 1 mil elementos
tempo_1k = testar_bubble_sort(1000)
print(f"Tempo para 1 mil elementos: {tempo_1k:.4f} segundos")

# Teste com 10 mil elementos
tempo_10k = testar_bubble_sort(10000)
print(f"Tempo para 10 mil elementos: {tempo_10k:.4f} segundos")

# O Bubble Sort tem complexidade O(n^2), o que significa que o tempo de execução cresce
# quadraticamente com o tamanho da entrada. Para 1 mil elementos, ele realiza cerca de 
# 1 milhão de comparações, enquanto para 10 mil elementos, faz cerca de 100 milhões.
# Isso explica por que o tempo aumenta drasticamente à medida que a lista cresce. 
# Em casos grandes, o Bubble Sort é ineficiente comparado a algoritmos mais rápidos como o Merge Sort.

# Algoritmo 1: Percorre a lista uma vez (O(n))
def soma_uma_passada(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

# Algoritmo 2: Percorre a lista duas vezes (O(2n))
def soma_duas_passadas(lista):
    primeira_soma = 0
    for numero in lista:
        primeira_soma += numero
    segunda_soma = 0
    for numero in lista:
        segunda_soma += numero
    return primeira_soma  # Retorna a soma apenas uma vez para manter o mesmo resultado

# Teste com uma lista de números
numeros = [1, 2, 3, 4, 5]
print(soma_uma_passada(numeros))
print(soma_duas_passadas(numeros))

# Ambos os algoritmos têm complexidade O(n) porque, na notação Big O, ignoramos constantes
# e nos concentramos na taxa de crescimento à medida que o tamanho da entrada aumenta.
# O(2n) é equivalente a O(n) porque o fator constante "2" não afeta a ordem de crescimento.
# Na prática, o algoritmo que percorre a lista uma vez é mais rápido, pois faz menos operações,
# mesmo que ambos tenham a mesma complexidade assintótica.
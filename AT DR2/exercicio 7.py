# Algoritmo otimizado para verificar duplicatas usando um hashtable
def verificar_duplicatas(lista):
    elementos = set()  # Usamos um conjunto (hashtable) para armazenar os elementos
    for item in lista:
        if item in elementos:
            return True  # Duplicata encontrada
        elementos.add(item)
    return False  # Nenhuma duplicata encontrada

# Exemplo de uso
lista_teste = [1, 2, 3, 4, 5, 6, 3]
resultado = verificar_duplicatas(lista_teste)
print(f"Há duplicatas? {resultado}")

# O algoritmo original tinha complexidade O(n^2) porque, para cada elemento, ele comparava com todos os outros.
# Com o uso de um hashtable (conjunto em Python), conseguimos verificar e inserir elementos em tempo O(1).
# Isso reduz a complexidade geral do algoritmo para O(n), pois percorremos a lista apenas uma vez.
# A escolha do hashtable é ideal aqui porque ele permite buscas rápidas e é eficiente para verificar duplicatas.
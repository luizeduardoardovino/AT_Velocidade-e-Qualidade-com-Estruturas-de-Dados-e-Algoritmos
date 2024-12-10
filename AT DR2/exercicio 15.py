# Implementação de uma Árvore Binária de Busca (BST) com operações para encontrar mínimo e máximo
class Nodo:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = Nodo(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, nodo, chave):
        if chave < nodo.chave:
            if nodo.esquerda is None:
                nodo.esquerda = Nodo(chave)
            else:
                self._inserir_recursivo(nodo.esquerda, chave)
        elif chave > nodo.chave:
            if nodo.direita is None:
                nodo.direita = Nodo(chave)
            else:
                self._inserir_recursivo(nodo.direita, chave)

    def encontrar_minimo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.chave

    def encontrar_maximo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.chave

# Exemplo de uso
notas = [85, 70, 95, 60, 75, 90, 100]
arvore = BST()

# Inserindo as notas na árvore
for nota in notas:
    arvore.inserir(nota)

# Encontrando o mínimo e o máximo
nota_minima = arvore.encontrar_minimo()
nota_maxima = arvore.encontrar_maximo()

print(f"Nota mínima: {nota_minima}")
print(f"Nota máxima: {nota_maxima}")

# Explicação:
# A Árvore Binária de Busca (BST) organiza as notas de forma que a nota mínima esteja no nó 
# mais à esquerda e a nota máxima no nó mais à direita. Para encontrar o mínimo, percorremos
# a subárvore esquerda até o último nó. Para o máximo, percorremos a subárvore direita. Ambas
# as operações têm complexidade O(h), onde 'h' é a altura da árvore. Em árvores balanceadas,
# essa altura é aproximadamente O(log n), tornando as buscas eficientes.

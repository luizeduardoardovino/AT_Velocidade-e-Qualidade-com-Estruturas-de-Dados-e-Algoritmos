# Implementação de uma Árvore Binária de Busca (BST) com operação de remoção
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

    def remover(self, chave):
        self.raiz = self._remover_recursivo(self.raiz, chave)

    def _remover_recursivo(self, nodo, chave):
        if nodo is None:
            return nodo

        if chave < nodo.chave:
            nodo.esquerda = self._remover_recursivo(nodo.esquerda, chave)
        elif chave > nodo.chave:
            nodo.direita = self._remover_recursivo(nodo.direita, chave)
        else:
            # Caso 1: Nó folha ou com um filho
            if nodo.esquerda is None:
                return nodo.direita
            elif nodo.direita is None:
                return nodo.esquerda

            # Caso 2: Nó com dois filhos
            sucessor = self._minimo(nodo.direita)
            nodo.chave = sucessor.chave
            nodo.direita = self._remover_recursivo(nodo.direita, sucessor.chave)

        return nodo

    def _minimo(self, nodo):
        atual = nodo
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def exibir_em_ordem(self):
        def _em_ordem(nodo):
            if nodo is not None:
                _em_ordem(nodo.esquerda)
                print(nodo.chave, end=" ")
                _em_ordem(nodo.direita)
        _em_ordem(self.raiz)
        print()

# Exemplo de uso
codigos = [45, 25, 65, 20, 30, 60, 70]
arvore = BST()

# Inserindo os códigos na árvore
for codigo in codigos:
    arvore.inserir(codigo)

# Exibindo a árvore em ordem crescente
print("Árvore em ordem crescente:")
arvore.exibir_em_ordem()

# Removendo os códigos e exibindo após cada remoção
print("\nRemovendo 20 (nó folha):")
arvore.remover(20)
arvore.exibir_em_ordem()

print("\nRemovendo 25 (nó com um filho):")
arvore.remover(25)
arvore.exibir_em_ordem()

print("\nRemovendo 45 (nó com dois filhos):")
arvore.remover(45)
arvore.exibir_em_ordem()

# Explicação:
# A remoção na Árvore Binária de Busca (BST) lida com três casos:
# 1. Nó folha: Simplesmente removemos o nó.
# 2. Nó com um filho: Substituímos o nó pelo seu único filho.
# 3. Nó com dois filhos: Substituímos o nó pelo sucessor (menor valor na subárvore direita),
# garantindo que a propriedade da BST seja mantida.
# A exibição em ordem crescente é feita por um percurso em ordem (in-order traversal),
# que tem complexidade O(n), onde 'n' é o número de nós.

# Implementação de uma Árvore Binária de Busca (BST)
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

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, nodo, chave):
        if nodo is None:
            return False
        if chave == nodo.chave:
            return True
        elif chave < nodo.chave:
            return self._buscar_recursivo(nodo.esquerda, chave)
        else:
            return self._buscar_recursivo(nodo.direita, chave)

# Exemplo de uso
precos = [100, 50, 150, 30, 70, 130, 170]
arvore = BST()

# Inserindo preços na BST
for preco in precos:
    arvore.inserir(preco)

# Buscando o preço 70
resultado = arvore.buscar(70)
print(f"O preço 70 está disponível? {'Sim' if resultado else 'Não'}")

# Explicação:
# A Árvore Binária de Busca (BST) organiza os preços de forma hierárquica: cada nó armazena
# uma chave (preço), e os valores menores vão para a subárvore esquerda, enquanto os maiores
# vão para a direita. Isso torna as operações de busca e inserção mais rápidas, com
# complexidade média O(log n) em árvores balanceadas. No entanto, em casos de árvores
# desbalanceadas, a complexidade pode chegar a O(n).

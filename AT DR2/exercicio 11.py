# Implementação de uma fila para gerenciar os chamados
from collections import deque

class FilaDeAtendimento:
    def __init__(self):
        self.fila = deque()  # Usamos deque para simular a fila

    def adicionar_chamado(self, chamado):
        self.fila.append(chamado)  # Adiciona o chamado ao final da fila
        print(f"Chamado '{chamado}' adicionado à fila")

    def atender_chamado(self):
        if not self.fila:
            print("Não há chamados na fila para atender")
            return
        chamado = self.fila.popleft()  # Remove o chamado do início da fila
        print(f"Atendendo chamado: {chamado}")

    def exibir_fila(self):
        if not self.fila:
            print("A fila está vazia")
        else:
            print("Chamados na fila:", list(self.fila))

# Exemplo de uso
fila = FilaDeAtendimento()
fila.adicionar_chamado("Chamado 1")
fila.adicionar_chamado("Chamado 2")
fila.adicionar_chamado("Chamado 3")
fila.exibir_fila()
fila.atender_chamado()
fila.exibir_fila()
fila.atender_chamado()
fila.atender_chamado()
fila.atender_chamado()

# A fila é a estrutura ideal para gerenciar chamados em um sistema de atendimento, pois segue
# o princípio FIFO (First In, First Out). Os chamados são atendidos na ordem em que chegam,
# garantindo justiça e organização no atendimento. Usamos deque porque ele é eficiente para
# operações de adição no final e remoção no início, ambas com complexidade O(1).

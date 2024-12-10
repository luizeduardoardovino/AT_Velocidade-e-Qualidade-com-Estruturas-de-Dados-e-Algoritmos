# Implementação de uma pilha para o sistema de navegação
class Navegador:
    def __init__(self):
        self.pilha_voltar = []  # Pilha para armazenar o histórico de páginas
        self.pilha_avancar = []  # Pilha para armazenar páginas para avançar

    def acessar_pagina(self, pagina):
        self.pilha_voltar.append(pagina)
        self.pilha_avancar.clear()  # Limpa a pilha de avançar ao acessar uma nova página
        print(f"Acessando: {pagina}")

    def voltar(self):
        if not self.pilha_voltar:
            print("Não há páginas para voltar")
            return
        pagina_atual = self.pilha_voltar.pop()
        self.pilha_avancar.append(pagina_atual)
        if self.pilha_voltar:
            print(f"Voltando para: {self.pilha_voltar[-1]}")
        else:
            print("Início do histórico")

    def avancar(self):
        if not self.pilha_avancar:
            print("Não há páginas para avançar")
            return
        pagina_atual = self.pilha_avancar.pop()
        self.pilha_voltar.append(pagina_atual)
        print(f"Avançando para: {pagina_atual}")

# Exemplo de uso
navegador = Navegador()
navegador.acessar_pagina("Página 1")
navegador.acessar_pagina("Página 2")
navegador.acessar_pagina("Página 3")
navegador.voltar()
navegador.voltar()
navegador.avancar()

# A pilha é uma estrutura de dados ideal para o sistema de navegação, pois segue o princípio
# LIFO (Last In, First Out). Quando o usuário acessa uma nova página, ela é adicionada ao topo
# da pilha de voltar. Ao usar o botão "Voltar", a página atual é removida da pilha de voltar
# e colocada na pilha de avançar. Da mesma forma, o botão "Avançar" remove a página do topo
# da pilha de avançar e a adiciona de volta na pilha de voltar. Isso garante um controle eficiente
# do histórico de navegação.

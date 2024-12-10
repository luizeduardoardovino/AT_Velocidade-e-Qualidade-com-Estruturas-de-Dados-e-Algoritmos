def busca_linear(lista_contatos, nome_procurado):
    for contato in lista_contatos:
        if contato['nome'] == nome_procurado:
            return contato['telefone']
    return "Contato não encontrado"

# Exemplo de uso
contatos = [
    {"nome": "Ana", "telefone": "1234-5678"},
    {"nome": "Bruno", "telefone": "2345-6789"},
    {"nome": "Carla", "telefone": "3456-7890"}
]

nome = "Bruno"
resultado = busca_linear(contatos, nome)
print(resultado)

# O algoritmo percorre a lista de contatos um por um (busca linear). Ele compara o nome
# de cada contato com o nome procurado. Se encontrar, retorna o telefone. Se não encontrar,
# retorna uma mensagem dizendo que o contato não foi achado.

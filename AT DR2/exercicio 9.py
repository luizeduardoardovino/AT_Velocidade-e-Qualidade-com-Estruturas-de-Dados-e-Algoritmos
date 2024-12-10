# Implementação usando uma hashtable para armazenar perfis
def armazenar_perfis(perfis):
    hashtable = {}
    for perfil in perfis:
        hashtable[perfil['username']] = perfil
    return hashtable

def recuperar_perfil(hashtable, username):
    return hashtable.get(username, "Perfil não encontrado")

# Exemplo de uso
perfis = [
    {"username": "joao123", "nome": "João Silva", "idade": 25},
    {"username": "ana456", "nome": "Ana Costa", "idade": 30},
    {"username": "carlos789", "nome": "Carlos Souza", "idade": 22}
]

# Armazenando perfis em uma hashtable
tabela = armazenar_perfis(perfis)

# Recuperando um perfil
resultado = recuperar_perfil(tabela, "ana456")
print(resultado)

# A abordagem com hashtable permite armazenar e recuperar informações em O(1), ou seja,
# tempo constante, independentemente do tamanho da lista de perfis. Em contraste, uma busca
# sequencial em uma lista tem complexidade O(n), pois precisa percorrer todos os elementos
# até encontrar o desejado (ou confirmar que ele não existe). Isso torna a hashtable muito
# mais eficiente para grandes conjuntos de dados.

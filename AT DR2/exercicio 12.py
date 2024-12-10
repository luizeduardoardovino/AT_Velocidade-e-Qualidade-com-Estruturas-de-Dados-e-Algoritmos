import os

# Função recursiva para listar arquivos em subdiretórios
def listar_arquivos_recursivamente(caminho):
    try:
        # Lista o conteúdo do diretório atual
        for item in os.listdir(caminho):
            caminho_completo = os.path.join(caminho, item)
            if os.path.isdir(caminho_completo):
                # Se for um diretório, chama a função recursivamente
                listar_arquivos_recursivamente(caminho_completo)
            elif os.path.isfile(caminho_completo):
                # Se for um arquivo, exibe o nome do arquivo
                print(caminho_completo)
    except PermissionError:
        print(f"Permissão negada para acessar: {caminho}")

# Exemplo de uso
# Substitua "caminho_da_pasta" por um caminho real em seu sistema
caminho_da_pasta = "./"
listar_arquivos_recursivamente(caminho_da_pasta)

# A recursão é uma abordagem natural para explorar diretórios aninhados porque ela resolve
# o problema de forma hierárquica. Para cada diretório, a função processa os arquivos e,
# caso encontre um subdiretório, faz uma nova chamada recursiva para explorá-lo. Assim, 
# ela vai "descendo" na estrutura de diretórios até atingir o nível mais profundo e, em 
# seguida, volta subindo até processar todos os itens. Isso evita a necessidade de criar
# laços complexos ou gerenciar manualmente uma pilha de diretórios.

# Implementação do problema da mochila usando programação dinâmica
def knapsack(pesos, valores, capacidade):
    n = len(pesos)
    # Criação da matriz para armazenar os resultados parciais
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenchendo a matriz dp
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                # Escolhe o máximo entre incluir ou não o item atual
                dp[i][w] = max(dp[i - 1][w], valores[i - 1] + dp[i - 1][w - pesos[i - 1]])
            else:
                # Não pode incluir o item atual
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]

# Exemplo de uso
pesos = [2, 3, 4, 5]  # Pesos dos itens
valores = [3, 4, 5, 6]  # Valores dos itens
capacidade = 8  # Capacidade máxima da mochila
resultado = knapsack(pesos, valores, capacidade)
print(f"Valor máximo que pode ser carregado: {resultado}")

# Explicação:
# A solução recursiva resolve o problema calculando repetidamente os mesmos subproblemas,
# o que leva a uma complexidade exponencial O(2^n).
# Usando programação dinâmica, armazenamos os resultados de subproblemas já resolvidos
# em uma matriz (memoização tabular), evitando recomputações desnecessárias.
# A complexidade da abordagem dinâmica é O(n * capacidade), onde 'n' é o número de itens,
# muito mais eficiente que a recursão simples para entradas maiores.

from mpmath import mp

def encontrar_sequencia_em_pi(sequencia):
    """
    Função para encontrar uma sequência numérica dentro das casas decimais de pi.

    Parâmetros:
    sequencia (str): A sequência de dígitos que se deseja encontrar em pi.

    Retorna:
    str: Mensagem informando em quantas casas decimais a sequência foi encontrada.
    """

    casas_decimais = 1  # Inicializa a quantidade de casas decimais de pi a serem consideradas
    sequencia_encontrada = False  # Flag para indicar se a sequência foi encontrada

    # Loop continua aumentando a precisão até encontrar a sequência
    while not sequencia_encontrada:
        mp.dps = casas_decimais  # Define a precisão decimal do cálculo de pi
        pi_str = str(mp.pi)       # Converte pi em string para permitir busca de substring

        # Percorre a string de pi verificando se a sequência está presente
        for i in range(len(pi_str) - len(sequencia) + 1):
            if pi_str[i:i+len(sequencia)] == sequencia:
                sequencia_encontrada = True
                break

        # Caso a sequência não tenha sido encontrada, aumenta a quantidade de casas decimais para próxima iteração
        if not sequencia_encontrada:
            casas_decimais += 10000

    return f"A sequência '{sequencia}' foi encontrada nas primeiras {casas_decimais} casas decimais de pi."

# Exemplo de uso:
sequencia_procurada = [4, 1, 14, 9, 5, 12]  # Sequência numérica a ser buscada (exemplo)
sequencia_str = ''.join(map(str, sequencia_procurada))  # Converte lista de números em string concatenada
resultado = encontrar_sequencia_em_pi(sequencia_str)  # Executa a busca pela sequência em pi
print(resultado)  # Imprime o resultado

from mpmath import mp

def encontrar_sequencia_em_pi(sequencia):
    casas_decimais = 1  # Inicie com 1 casa decimal
    sequencia_encontrada = False

    while not sequencia_encontrada:
        mp.dps = casas_decimais
        pi_str = str(mp.pi)

        for i in range(len(pi_str) - len(sequencia) + 1):
            if pi_str[i:i+len(sequencia)] == sequencia:
                sequencia_encontrada = True
                break

        if not sequencia_encontrada:
            casas_decimais += 10000

    return f"A sequência '{sequencia}' foi encontrada nas primeiras {casas_decimais} casas decimais de pi."

# Exemplo de uso:
sequencia_procurada = [4, 1, 14, 9, 5, 12]  # Por exemplo, procurando a sequência '12345'
sequencia_str = ''.join(map(str, sequencia_procurada))
resultado = encontrar_sequencia_em_pi(sequencia_str)
print(resultado)

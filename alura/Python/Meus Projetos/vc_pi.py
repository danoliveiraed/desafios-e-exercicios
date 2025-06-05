

from mpmath import mp


def imprime_abertura():
    print('===================================')
    print('============Bem vindo ao:==========')
    print('===Encontre seu nome dentro de pi==')
    print('===================================')
def seu_nome():
    busca = input('Digite seu nome: ')
    busca = busca.strip().upper()
    return busca

def converter(busca):
    numeros = []

    for letra in busca:
        if letra.isalpha():
            numero_letra = ord(letra) - ord('A') + 1
            numeros.append(numero_letra)
        # elif letra.isspace():
        #     numeros.append(0)

    return numeros

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
            casas_decimais += 500000

    return f"A sequência '{sequencia}' foi encontrada nas primeiras {casas_decimais} casas decimais de pi."


imprime_abertura()
nome = seu_nome()
sequencia = converter(nome)
print(nome)
print(sequencia)
sequencia_procurada = sequencia  # Por exemplo, procurando a sequência '12345'
sequencia_str = ''.join(map(str, sequencia_procurada))
resultado = encontrar_sequencia_em_pi(sequencia_str)
print(resultado)

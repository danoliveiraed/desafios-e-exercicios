from mpmath import mp

def imprime_abertura():
    """
    Imprime a mensagem de abertura do programa na tela.
    """
    print('===================================')
    print('============Bem vindo ao:==========')
    print('===Encontre seu nome dentro de pi==')
    print('===================================')

def seu_nome():
    """
    Solicita ao usuário que digite seu nome, 
    remove espaços extras e converte para letras maiúsculas.

    Retorna:
    str: Nome formatado em letras maiúsculas e sem espaços extras.
    """
    busca = input('Digite seu nome: ')
    busca = busca.strip().upper()
    return busca

def converter(busca):
    """
    Converte uma string contendo letras em uma lista de números 
    correspondentes à posição da letra no alfabeto (A=1, B=2, ..., Z=26).

    Parâmetros:
    busca (str): Nome a ser convertido.

    Retorna:
    list: Lista de inteiros correspondentes às letras do nome.
    """
    numeros = []

    for letra in busca:
        if letra.isalpha():
            numero_letra = ord(letra) - ord('A') + 1  # Converte letra para número (A=1)
            numeros.append(numero_letra)
        # Caso queira tratar espaços, pode descomentar o trecho abaixo:
        # elif letra.isspace():
        #     numeros.append(0)

    return numeros

def encontrar_sequencia_em_pi(sequencia):
    """
    Busca uma sequência de dígitos nas casas decimais de pi, aumentando progressivamente
    o número de casas decimais verificadas até encontrar a sequência.

    Parâmetros:
    sequencia (str): Sequência de números a ser buscada (como string).

    Retorna:
    str: Mensagem indicando em quantas casas decimais a sequência foi encontrada.
    """
    casas_decimais = 1  # Inicia com 1 casa decimal de pi
    sequencia_encontrada = False  # Flag para controlar busca

    while not sequencia_encontrada:
        mp.dps = casas_decimais  # Define a precisão decimal para o cálculo de pi
        pi_str = str(mp.pi)       # Converte pi para string para busca de substring

        # Verifica se a sequência está presente na string de pi
        for i in range(len(pi_str) - len(sequencia) + 1):
            if pi_str[i:i+len(sequencia)] == sequencia:
                sequencia_encontrada = True
                break

        # Caso não encontre, aumenta o número de casas decimais para a próxima busca
        if not sequencia_encontrada:
            casas_decimais += 500000

    return f"A sequência '{sequencia}' foi encontrada nas primeiras {casas_decimais} casas decimais de pi."


# Fluxo principal do programa
imprime_abertura()                # Exibe a mensagem de abertura
nome = seu_nome()                 # Recebe o nome do usuário
sequencia = converter(nome)       # Converte o nome em sequência numérica
print(nome)                      # Imprime o nome formatado
print(sequencia)                 # Imprime a lista numérica correspondente ao nome
sequencia_procurada = sequencia  # Sequência que será buscada em pi
sequencia_str = ''.join(map(str, sequencia_procurada))  # Converte lista para string
resultado = encontrar_sequencia_em_pi(sequencia_str)    # Busca a sequência em pi
print(resultado)                 # Exibe o resultado da busca


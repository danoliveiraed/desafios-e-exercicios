import random
#===========funções====================================
def imprime_mess_abertura():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def pede_chute():
    chute = input("Qual letra?: ")
    chute = chute.strip().upper()  # strip limpa espaços na digitação
    return chute


def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mess_sucesso():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mess_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros, limite):
    print("Erros {}/{}".format(erros, limite))
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
#===========funções fim=================================
def jogar(): #definir como módulo

    imprime_mess_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou  = False
    erros = 0
    limite = 7
    letras_erradas = []

    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)#vars não estão na função, por isso passa por params
        else:
            letras_erradas.append(chute)
            erros += 1
            desenha_forca(erros, limite)
        enforcou = erros == limite
        acertou = "_" not in letras_acertadas



        print("Letras acertadas: ", letras_acertadas)
        print("Letras erradas: ", letras_erradas)



    if(acertou):
        imprime_mess_sucesso()
    else:
        imprime_mess_derrota(palavra_secreta)

    print("Fim do Jogo!")

if(__name__ == "__main__"): #permite que programa funcione individualmente
    jogar()

    #módulos e funções
import random
def jogar(): #definir como módulo

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    #---------------------
    #variaveis de controle
    #---------------------
    numero_secreto = random.randrange(1,101)
    c_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        c_tentativas = 20
    elif(nivel == 2):
        c_tentativas = 10
    else:
        c_tentativas = 5

    #---------------------
    #laço de repetição
    #---------------------
    for rodada in range(1, c_tentativas + 1):
    #variaveis do laço
        print("Tentativa {}/{}".format(rodada, c_tentativas))

        chute_str=input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute=int(chute_str)

        if(chute < 1 or chute > 100):
            print("Vocẽ deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto
    #------------------------
        if(acertou):
            print("Acertou e fez {} pontos!!".format(pontos))
            break
        else:
            if(maior):
                print("Errou!! Chute maior que número secreto.")
                if(rodada == c_tentativas):
                    print("O número secreto era {}. Você fez {} pontos!".format(numero_secreto, pontos))
            elif(menor):
                print("Errou!! Chute menor que número secreto.")
                if (rodada == c_tentativas):
                    print("O número secreto era {}. Você fez {} pontos!".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1
    #fim do laço de repetição
    #print("O número secreto é: ", numero_secreto)
    print("Fim do Jogo!")

if(__name__ == "__main__"): #permite que programa funcione individualmente
    jogar()
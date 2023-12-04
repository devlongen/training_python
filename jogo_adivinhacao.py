import random

loop_adivinha = True
tentativas = 3
numero_aleatorio = random.randint(1,100)
while loop_adivinha:
    print("-=Seja bem vindo ao jogo de adivinhação em Python=-")
    print("   Para começarmos preciso de suas informações  ")
    nome_usuario = str(input("Diga o seu nome >"))
    idade_usuario = int(input("Diga a sua idade >"))
    while True:
        resposta_usuario = str(input("Vamos comecar a jogar? (sim ou nao)"))
        if resposta_usuario == "sim":
            break
        elif resposta_usuario == "nao":
            print("Espero que tenha um bom dia!")
            loop_adivinha = False
            break
        else:
            print("Escreveu algo invalido ou algo diferente de sim ou nao")
    while tentativas:
        tentativa_jogador = int(input("Voce tera 3 tentativas de acertar um numero aleatorio de 1 ate 100, BOA SORTE!"))
        if tentativa_jogador == numero_aleatorio:
            print("Parabens voce acertou o numero!")
            loop_adivinha = False
        elif tentativa_jogador < numero_aleatorio:
            print("Esta perto o numero e maior!")
            tentativas = tentativas - 1
        else:
            print("Esta perto o numero e menor!")
            tentativas = tentativas - 1
    
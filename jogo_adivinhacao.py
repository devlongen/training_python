loop_adivinha = True
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
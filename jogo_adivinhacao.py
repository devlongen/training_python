import random

loop_adivinha = True
tentativas = 3
numero_aleatorio = random.randint(1,100)
while loop_adivinha:
    print("-=Seja bem vindo ao jogo de adivinhação em Python=-")
    print("   Para começarmos preciso de suas informações  ")
    nome_usuario = str(input("Diga o seu nome >"))
    while True:
        idade_usuario = int(input("Diga a sua idade >"))
        if 0 <= idade_usuario <= 99:
            break
        else:
            print("Idade inválida você inseriu um valor não congruente!")
    while True:
        resposta_usuario = str(input("Vamos comecar a jogar? (sim ou não)"))
        if resposta_usuario == "sim":
            break
        elif resposta_usuario == "não":
            print("Espero que tenha um bom dia!")
            loop_adivinha = False
            break
        else:
            print("Escreveu algo inválido ou algo diferente de sim ou não")
    while tentativas:
        tentativa_jogador = int(input("Você terá 3 tentativas de acertar um número aleatório de 1 até 100, BOA SORTE!"))
        if tentativa_jogador == numero_aleatorio:
            print("Parabéns! Você acertou o número!")
            loop_adivinha = False
        elif tentativa_jogador < numero_aleatorio:
            print("Você está perto, mas o número é maior!")
        else:
            print("Você está perto, mas o número é menor!")
        tentativas -= 1
        if tentativas == 0:
            print(f"Fim das tentativas. O número era {numero_aleatorio}.")
            loop_adivinha = False
    

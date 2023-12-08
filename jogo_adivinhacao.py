# ajustar o número que aparece na tela, jogo funcionando porém precisa de validações

import random
#biblioteca de randomizar numero
loop_adivinha = True
# declaração das constantes
# código do jogo de adivinhação
while loop_adivinha:
    tentativas = 3
    numero_aleatorio = random.randint(1,100)
    numero_proximo = numero_aleatorio
# declaracao de variaveis que nao sao constantes
    print("-=Seja bem vindo ao jogo de adivinhação em Python=-")
    print("   Para começarmos preciso de suas informações  ")
    nome_usuario = str(input("Diga o seu nome >"))
    while True:
        idade_usuario = int(input("Diga a sua idade >"))
        if 0 <= idade_usuario <= 99:
            break
        else:
            print("Idade inválida você inseriu um valor não congruente!")
# pedindo e validando as informações pessoais do usuário
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
# pedindo e validando as informações para jogar do usuário
    while tentativas:
        tentativa_jogador = int(input("Você terá 3 tentativas de acertar um número aleatório de 1 até 100, BOA SORTE!"))
        if tentativa_jogador == numero_aleatorio:
            print("Parabéns! Você acertou o número!")
            loop_adivinha = False
            break
        elif tentativa_jogador > numero_aleatorio:
            numero_proximo = numero_aleatorio + 5
            print("Boa tentativa, mas o número é menor que:", numero_proximo)
        else:
            numero_proximo = numero_aleatorio - 3
            print("Boa tentativa, mas o número é maior que:", numero_proximo)
        tentativas -= 1
        if tentativas == 0:
            print(f"Fim das tentativas. O número era {numero_aleatorio}.")
            loop_adivinha = False
# funcionamento do jogo e as tentativas
    while True:
        resposta_recomecar = str(input("Você deseja tentar novamente? (sim ou não)"))
        if resposta_recomecar == "sim":
            loop_adivinha = True
            break
        elif resposta_recomecar == "não":
            print("Espero que tenha gostado do jogo!")
            loop_adivinha = False
        else:
            print("Você digitou algo inválido ou que não condiz com a pergunta, tente novamente!")
# perguntando para o usuário caso deseja tentar novamente

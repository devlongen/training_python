loop_calculadora = True
while loop_calculadora:
    nome_usuario = str(input("Escreva o seu nome > "))
        try:
            idade_usuario = int(input("Digite a sua idade > "))
            if idade_usuario >= 0 and idade_usuario <= 100:
                break
            else:
                print("Erro: número inválido")
        except ValueError as e:
            peso_usuario = float(input("Digite o seu peso em kg > "))
        if peso_usuario >= 0 and peso_usuario <= 500.00:
            break
        else:
            print("Erro: número inválido")
    except ValueError as e:
        altura_usuario = float(input("Digite a sua altura em metros > "))
        if altura_usuario >= 0 and altura_usuario <= 2.20:
            break
        else:
            print("Erro: número inválido")
    except ValueError as e:
resposta_usuario = str(input("Vamos calcular o seu imc? (sim ou não)"))
    if resposta_usuario == 'sim':
            resultado_imc = peso_usuario / (altura_usuario *
            altura_usuario)
            print("Seu calculo ficou entre o valor:",
            resultado_imc)
    else:
         print("Tudo bem, tenha um bom dia!")
    resposta_loop = str(input("Deseja continuar? s/n"))
    loop_calculadora = resposta_loop.lower() == 's'




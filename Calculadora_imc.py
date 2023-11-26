loop_calculadora = True

while loop_calculadora:
    nome_usuario = str(input("Escreva o seu nome > "))

    try:
        idade_usuario = int(input("Digite a sua idade > "))
        if 0 <= idade_usuario <= 100:
            break
        else:
            print("Erro: número inválido")
    except ValueError as e:
        print(f"Erro de valor: {e}")

while loop_calculadora:
    try:
        peso_usuario = float(input("Digite o seu peso em kg > "))
        if 0 <= peso_usuario <= 500.00:
            break
        else:
            print("Erro: número inválido")
    except ValueError as e:
        print(f"Erro de valor: {e}")

while loop_calculadora:
    try:
        altura_usuario = float(input("Digite a sua altura em metros > "))
        if 0 <= altura_usuario <= 2.20:
            break
        else:
            print("Erro: número inválido")
    except ValueError as e:
        print(f"Erro de valor: {e}")

resposta_usuario = str(input("Vamos calcular o seu IMC? (sim ou não)"))
if resposta_usuario.lower() == 'sim':
    resultado_imc = peso_usuario / (altura_usuario * altura_usuario)
    print("Seu cálculo ficou entre o valor:", resultado_imc)
else:
    print("Tudo bem, tenha um bom dia!")

resposta_loop = str(input("Deseja continuar? s/n"))
loop_calculadora = resposta_loop.lower() == 's'





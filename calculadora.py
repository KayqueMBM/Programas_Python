def calculadora():
    print("Bem vindo a calculadora!")
    print("Escolha uma operação")
    print("1. Soma")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")

    operacao = input("Digite o número da operação (1/2/3/4):")

    if operacao in ['1', '2', '3', '4']:
        try:
            valor1 = int(input("Digite o primeiro número:"))
            valor2 = int(input("Digite o segundo número: "))

            if operacao == '1':
                print(f"Resultado: {valor1} + {valor2} = {valor1 + valor2}")
            elif operacao == '2':
                print(f"Resultado: {valor1} - {valor2} = {valor1 - valor2}")
            elif operacao == '3':
                print(f"Resultado: {valor1} / {valor2} = {valor1 / valor2}")
            elif operacao == '4':
                print(f"Resultado: {valor1} * {valor2} = {valor1 * valor2}")
        except ValueError:
            print("Valor inserido incorreto!")
    else:
        print("Escolha um número válido")

calculadora()
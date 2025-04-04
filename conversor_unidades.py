def conversor_unidades():
    print("Escolha uma opção:")
    print("1. Metros para Quilômetros")
    print("2. Quilômetros para Metros")
    print("3. Metros para Centímetros")
    print("4. Centímetros para Metros")

    escolha = int(input("Digite o número da opção:"))
    valor = float(input("Digite o valor a ser convertido:"))

    if escolha == 1:
        resultado = valor / 1000
        print(f"{valor} metros equivalem a {resultado} quilômetros")
    elif escolha == 2:
        resultado = valor * 1000
        print(f"{valor} quilômetros equivalem a {resultado} metros")
    elif escolha == 3:
        resultado = valor * 100
        print(f"{valor} metros equivalem a {resultado} centímetros")
    elif escolha == 4:
        resultado = valor / 100
        print(f"{valor} centímetros equivalem a {resultado} metros")
    else:
        print("Opção inválida!")

conversor_unidades()
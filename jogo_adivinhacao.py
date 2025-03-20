import random
def jogo_adivinhação():
    print("Bem vindo ao jogo de adivinhação!")

    numero_secreto = random.randint(1, 10) # Gera números de 1 á 10

    while True:
        try:
            sugestao = int(input("Digite sua sugestão de número:"))

            if sugestao < numero_secreto:
                print("Número menor que o número escolhido")
            elif sugestao > numero_secreto:
                print("Número maior que o número escolhido")
            else:
                print("Parabêns você acertou o número secreto")
                break
        except ValueError:
            print("Valor inserido incorreto!")
            
# Executa o jogo
jogo_adivinhação()
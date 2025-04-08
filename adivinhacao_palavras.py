import random

palavras = ["computador", "tablet", "televisão", "celular", "notebook"]

# Escolher uma palavra aleatória
palavra_secreta = random.choice(palavras)

# Configurar o jogo
letras_descobertas = ["_" for letra in palavra_secreta]
tentativas_restantes = 6

print("Bem-vindo ao jogo de adivinhação de palavras!")
print(" ".join(letras_descobertas))

# Loop do jogo
while "_" in letras_descobertas and tentativas_restantes > 0:
    letra = input("\n Digite uma letra:").lower()

    if letra in palavra_secreta:
        for i, l in enumerate (palavra_secreta):
            if l == letra:
                letras_descobertas[i] = letra
        print("Boa! Você acertou uma letra")
    else:
        tentativas_restantes -= 1
        print(f"Ops, essa letra não está na palavra. Tentativas restantes: {tentativas_restantes}")
    
    print(" ".join(letras_descobertas))

# Fim de jogo
if "_" not in letras_descobertas:
    print("\n Parabêns! Você descobriu a palavra:", palavra_secreta)
else:
    print("\n Você perdeu! A palavra era:", palavra_secreta)
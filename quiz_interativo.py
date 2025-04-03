print("Bem-vindo ao Quiz Python")
pontuacao = 0 # Pontuação inicial

# Pergunta 1
print("\n1. Qual é a capital do Brasil?")
print("a) São Paulo")
print("b) Rio de Janeiro")
print("c) Brasília")
resposta1 = input("Sua resposta:")

if resposta1.lower() == "c" or "Brasília":
    print("Correto!")
    pontuacao += 1
else:
    print("Errado!, a resposta correta é: c) Brasília")

# Pergunta 2
print("\n2. Qual linguagem de programação eu usei para programar esse quiz?")
print("a) Java")
print("b) Python")
print("c) JavaScript")
resposta2 = input("Sua resposta:")

if resposta2.lower() == "b" or "Python":
    print("Correto!")
    pontuacao += 1
else:
    print("Errado!, a resposta correta é: b) Python")

# Pergunta 3
print("\n3. Quantos planetas tem no nosso sistema solar?")
print("a) 8")
print("b) 9")
print("c) 7")
resposta3 = input("Sua resposta:")

if resposta3.lower() == "a" or "8":
    print("Correto!")
    pontuacao += 1
else:
    print("Errado!, a resposta correta é: a) 8")

# Resultado final
print(f"\n Você acertou {pontuacao} de 3 perguntas.")
if pontuacao == 3:
    print("Parabéns, você é um gênio!")
elif pontuacao == 2:
    print("Bom trabalho, mas dá para melhorar!")
elif pontuacao == 1:
    print("Você pode melhorar, continue se esforçando!")
else:
    print("Vai estudar se quiser acertar pelo menos uma!")

print("Obrigado por jogar")
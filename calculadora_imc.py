# Calculadora IMC (Indíce de Massa Corporal)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
# Entrada do usuário
peso = float(input("Digite seu peso (em kg):"))
altura = float(input("Digite sua altura (em metros):"))

# Cálculo IMC
imc = calcular_imc(peso, altura)
categoria = classificar_imc(imc)

# Exibição de resultados
print(f"\n Seu IMC é: {imc: .2f}")
print(f"Você está na categoria: {categoria}")
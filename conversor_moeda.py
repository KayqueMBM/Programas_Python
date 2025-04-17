def conversor_moeda():
    valor = float(input("Digite o valor em reais (BRL):"))
    taxa_cambio = float(input("Digite a taxa de câmbio (exemplo: se a taxa de câmbio do dólar é 5,00, significa que um dólar dos Estados Unidos custa R$ 5,00.:"))

    valor_convertido = valor / taxa_cambio
    print(f"O valor convertido é: {valor_convertido: .2f} na moeda de destino.")

# Chamar a função
conversor_moeda()
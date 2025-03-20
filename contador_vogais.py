def contador_vogal(texto):
    
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1
    
    return contador

teclado = input("Digite algo que tenha vogais:")
numero_vogais = contador_vogal(teclado)
    
print(f"O número de vogais é: {numero_vogais}")
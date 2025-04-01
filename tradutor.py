from deep_translator import GoogleTranslator

# Texto para traduzir

texto = input("Digite algo para ser traduzido:")

# Realiza a tradução

traducao = GoogleTranslator(source = "pt", target = "en").translate(texto) # Português é o idioma origem e o inglês é o idioma destino

print("Texto original:", texto)
print("Tradução:", traducao)
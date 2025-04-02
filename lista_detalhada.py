#Cria a lista

carros = [{"marca": "Toyota", "modelo": "Corolla", "ano": 2023, "tipo": "Sedan"},
          {"marca": "Honda", "modelo": "Civic", "ano": 2022, "tipo": "Sedan"},
          {"marca": "Chevrolet", "modelo": "Onix", "ano": 2021, "tipo": "Hatch"},
          {"marca": "Ford", "modelo": "Fiesta", "ano": 2020, "tipo": "Hatch"},
          {"marca": "Hyundai", "modelo": "Creta", "ano": 2019, "tipo": "SUV"}]

# Exibe a lista

print("Lista de carros:")
for carro in carros:
    print(f"Marca: {carro["marca"]}, Modelo: {carro["modelo"]}, Ano: {carro["ano"]}, Tipo: {carro["tipo"]}")
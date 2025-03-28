import requests

def consultar_cep(cep):
    try:
        # Verifica se o CEP tem 8 dígitos

        if len(cep) != 8 or not cep.isdigit():
            return "CEP inválido. Certifique-se de digitar exatamente 8 números"
        
        # Faz a requisição para a API

        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)

        # Verifica se a resposta ta correta

        if resposta.status_code == 200:
            dados = resposta.json()

            # Verifica se tem erro

            if "erro" in dados:
                return "CEP não encontrado"
            
            # Retorna as informações do endereço

            return f"""
            Logradouro:{dados.get('logradouro', 'Não disponível')}
            Bairro:{dados.get('bairro', 'Não disponível')}
            Cidade:{dados.get('localidade', 'Não disponível')}
            Estado:{dados.get('uf', 'Não disponível')}
            """
        else:
            return "Erro ao consultar CEP"
    except Exception as e:
        return f"Ocorreu erro:{e}"
# Testa o sistema

cep = input("Digite um CEP (somente números):")
resultado = consultar_cep(cep)
print(resultado)
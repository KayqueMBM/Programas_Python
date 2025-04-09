class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []
    
    def adicionar_item(self, produto, quantidade):
        self.itens.append({"produto": produto, "quantidade": quantidade})

    def remover_item(self, produto):
        self.itens = [item for item in self.itens if item["produto"] != produto]
    
    def calcular_total(self):
        total = sum(item["produto"].preco * item["quantidade"] for item in self.itens)
        return total
    
    def mostrar_itens(self):
        print("Itens no carrinho:")
        for item in self.itens:
            print(f"{item['produto'].nome} - {item['quantidade']} unidade(s) - R$ {item['produto'].preco:.2f} cada")

# Exemplo de uso
    
produto1 = Produto("Maçã", 2.50)
produto2 = Produto("Banana", 1.80)

carrinho = Carrinho()
carrinho.adicionar_item(produto1, 3)
carrinho.adicionar_item(produto2, 5)

carrinho.mostrar_itens()
print(f"Total: R$ {carrinho.calcular_total():.2f}")
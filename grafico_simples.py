import matplotlib.pyplot as plt

# Dados para o gráfico
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Criando o gráfico
plt.plot(x, y, label = 'Gráfico de linha')

# Personalizações
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Meu Gráfico em Python')
plt.legend()

# Mostrando o gráfico
plt.show()
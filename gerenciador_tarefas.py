todas_tarefas = [] # Onde vai ficar todas as suas tarefas

def adicionar_tarefas(tarefa):
    todas_tarefas.append(tarefa)
    print(f"Tarefa adicionada: {tarefa}")

def remover_tarefas(indice):
    try:
        tarefa_removida = todas_tarefas.pop(indice - 1)
        print(f"Tarefa removida: {tarefa_removida}")
    except IndexError:
        print("Índice inválido")

def listar_tarefas():
    print("\nTarefas:")
    for i, tarefa in enumerate(todas_tarefas, 1):
        print(f"{i} {tarefa}")
    
while True:
        print("\nMenu:")
        print("1, Adiconar Tarefa")
        print("2, Remover Tarefa")
        print("3, Listar Tarefas")
        print("4, Sair")

        escolha = input("Escolha uma das opções:")

        if escolha == '1':
            tarefa = input("Digite a tarefa:")
            adicionar_tarefas(tarefa)
        
        elif escolha == '2':
            indice = int(input("Digite o número da tarefa para ser removida:"))
            remover_tarefas(indice)

        elif escolha == '3':
            listar_tarefas()

        elif escolha == '4':
            print("Você saiu!")
            break

        else:
            print("Opção inválida")
def chatbot():
    print("Olá!, eu sou o Chatbot")
    print("Digite 'sair' para encerrar a conversa.")

    while True:
        mensagem = input("Você:").lower()

        if mensagem == "sair":
            print("Chatbot: Até mais, foi ótimo conversar com você!")
            break
        elif "oi" in mensagem or "olá" in mensagem:
            print("Chatbot: Olá!, como posso ajudar você hoje?")
        elif "tudo bem" in mensagem:
            print("Chatbot: Sim. Eu gosto de ajudar!")
        else:
            print("Chatbot: Desculpe, não entendi.")

chatbot()
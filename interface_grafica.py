import customtkinter as ctk

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'kayque' and senha == '123':
        resultado_login.configure(text = 'Login feito com sucesso!', text_color = 'green')
    else:
        resultado_login.configure(text = 'Login ou senha incorretos!', text_color = 'red')

# Aparência
ctk.set_appearance_mode('dark')

# Interface principal
interface = ctk.CTk()
interface.title('Sistema de login')
interface.geometry('300x300')

# Campos
label_usuario = ctk.CTkLabel(interface, text = 'Usuário')
label_usuario.pack(pady = 10)

campo_usuario = ctk.CTkEntry(interface, placeholder_text = 'Digite seu usuário')
campo_usuario.pack(pady = 10)

label_senha = ctk.CTkLabel(interface, text = 'Senha')
label_senha.pack(pady = 10)

campo_senha = ctk.CTkEntry(interface, placeholder_text = 'Digite sua senha')
campo_senha.pack(pady = 10)

# Botão
botao = ctk.CTkButton(interface, text = 'Login', command = validar_login)
botao.pack(pady = 10)

# Validação do login
resultado_login = ctk.CTkLabel(interface, text = '')
resultado_login.pack(pady = 10)

# Executar interface gráfica
interface.mainloop()
import mysql.connector
from mysql.connector import Error

def conectar_ao_mysql(host, usuario, senha, banco):
    print("Tentando conectar ao MySQL...")
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = usuario,
            password = senha,
            database = banco
        )
        if conexao.is_connected():
            print("Conexão estabelecida com sucesso!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
    
def fechar_conexao(conexao):
    print("Tentando fechar a conexão...")
    if conexao and conexao.is_connected():
        conexao.close()
        print("Conexão com o MySQL foi encerrada.")
    else:
        print("Nenhuma conexão ativa para encerrar.")

# Exemplo de uso
if __name__ == "__main__":
    print("Iniciando o programa...")
    host = "localhost"
    usuario = "root"
    senha = ""
    banco = "banco_python"

    conexao = conectar_ao_mysql(host, usuario, senha, banco)
    if conexao:
        fechar_conexao(conexao)
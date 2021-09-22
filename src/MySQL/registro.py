import pymysql as py

class RegistroMySQL:
    def __init__(cls):
        # Criando conexão
        try:
            cls.con = py.connect(
                host="localhost",
                user="root",
                password="",
                database="action_stalker"
                )
        except:
            print("ERRO, Não Foi Possível Conectar ao Banco de Dados")


    """
    Função de verificação de registros
    retorna None, caso não haja o codigo no banco de dados
    retorna um valor não nulo, caso haja o código no bando de dados  
    """
    def verificacao_registros(cls, codigo):
        command = f"SELECT codigo, password FROM registros WHERE codigo=\"{codigo}\""
        cursor = cls.con.cursor()
        cursor.execute(command)

        pesq = cursor.fetchall()

        return pesq

    """
    Função de registro de registros
    retorna None, caso exista o código no banco de dados
    retorna True, caso o registro seja bem sucedido
    retorna False, caso ocorra um erro no registro   
    """
    def registrar_registros(cls, codigo, tipo):
        command = f"SELECT codigo FROM registros WHERE codigo=\"{codigo}\""
        cursor = cls.con.cursor()
        cursor.execute(command)

        pesq = cursor.fetchall()

        if pesq:
            return None
        else:
            command = "INSERT INTO registros(codigo, tipo, empresa) VALUES (%s, %s, %s)"
            valor = (codigo, tipo, "EMPRESA")

            try:
                cursor.execute(command, valor)
                cls.con.commit()
                return True
            except:
                return False

    """
    Função de registro de login
    retorna None, caso não exista elementos no banco de dados
    retorna True, caso exista elementos no banco de dados
    """
    def list_elements(cls):
        command = "SELECT * FROM registros"
        cursor = cls.con.cursor()
        cursor.execute(command)

        elements = cursor.fetchall()

        return elements

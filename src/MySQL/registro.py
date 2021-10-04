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
    retorna False, caso exista o código no banco de dados  
    """
    def registrar_registros(cls, codigo, indicadores):
        cursor = cls.con.cursor()

        try:
            command = "INSERT INTO registros(codigo, tipo, indicador_01, indicador_02, indicador_03, indicador_04, label_01, label_02, label_03, label_04) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valor = (codigo, indicadores[1], indicadores[0][0][1], indicadores[0][1][1], indicadores[0][2][1], indicadores[0][3][1], indicadores[0][0][0], indicadores[0][1][0], indicadores[0][2][0], indicadores[0][3][0])

            cursor.execute(command, valor)
            cls.con.commit()
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

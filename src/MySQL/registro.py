import pymysql as py


class RegistroMySQL:
    def __init__(cls):
        # Criando conexão
        try:
            cls.connection_codes = py.connect(
                host="localhost",
                user="root",
                password="",
                database="ACTION_STALKER_CODES"
                )
        except:
            print("ERRO, Não Foi Possível Conectar ao Banco de Dados")

    def registrar_registros(cls, codigo, indicadores, user):
        """
        Função de registro de registros
        retorna False, caso exista o código no banco de dados
        """
        cursor_codes = cls.connection_codes.cursor()

        try:
            command = f"INSERT INTO {user}(codigo, tipo, indicador_01, indicador_02, indicador_03, indicador_04,"
            command += " indicador_05, indicador_06) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            valor = (codigo, indicadores[1], indicadores[0][0], indicadores[0][1], indicadores[0][2], indicadores[0][3], indicadores[0][4], indicadores[0][5])

            cursor_codes.execute(command, valor)
            cls.connection_codes.commit()
        except:
            return False

    def list_elements(cls, user):
        """
        Função de registro de login
        retorna None, caso não exista elementos no banco de dados
        retorna True, caso exista elementos no banco de dados
        """
        command = f"SELECT * FROM {user}"
        cursor_codes = cls.connection_codes.cursor()
        cursor_codes.execute(command)

        elements = cursor_codes.fetchall()

        return elements

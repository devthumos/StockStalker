import pymysql as py


class LoginMySQL:
    def __init__(cls):
        # Criando conexão
        try:
            cls.connection_users = py.connect(
                host="localhost",
                user="root",
                password="",
                database="ACTION_STALKER_USERS"
                )

            cls.connection_codes = py.connect(
                host="localhost",
                user="root",
                password="",
                database="ACTION_STALKER_CODES"
            )
        except:
            print("ERRO, Não Foi Possível Conectar aos Bancos de Dados")

    def create_table_codeuser(cls, user):
        cursor_codes = cls.connection_codes.cursor()
        command = f"CREATE TABLE {user}(codigo VARCHAR(255), tipo VARCHAR(255), "
        command += "indicador_01 VARCHAR(255), indicador_02 VARCHAR(255), indicador_03 VARCHAR(255), "
        command += "indicador_04 VARCHAR(255), indicador_05 VARCHAR(255),indicador_06 VARCHAR(255), PRIMARY KEY(codigo))"
        cursor_codes.execute(command)

    def verificacao_login(cls, user, password):
        """
        Função de verificação de login
        retorna None, caso as credenciais sejam inválidas
        retorna um conteúdo, caso as credenciais sejam válidas
        """
        command = f"SELECT user, password FROM login WHERE user=\"{user}\" and password=\"{password}\""
        cursor_users =cls.connection_users.cursor()
        cursor_users.execute(command)

        pesq = cursor_users.fetchall()

        return pesq

    def registrar_login(cls, user, password):
        """
        Função de registro de login
        retorna None, caso exista o usuário no banco de dados
        retorna True, caso o registro seja bem sucedido
        retorna False, caso ocorra um erro no registro
        retorna
        """
        command = f"SELECT user FROM login WHERE user=\"{user}\""
        cursor_users = cls.connection_users.cursor()
        cursor_users.execute(command)

        pesq = cursor_users.fetchall()

        if pesq:
            return None
        else:
            command = "INSERT INTO login(user, password) VALUES (%s, %s)"
            valor = (user, password)

            try:
                cursor_users.execute(command, valor)
                cls.connection_users.commit()
                cls.create_table_codeuser(user)  # Criando a tabela de códigos para o usuáio em específico
                return True
            except:
                return False

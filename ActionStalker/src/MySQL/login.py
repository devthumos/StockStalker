import pymysql as py


class LoginMySQL:
    """
        Essa classe é responsável pela conexão aos 2 bancos de dados, pela verificação de login e criação das tabelas do
        action_stalker_codes de acordo com o id do usuário
        """
    def __init__(cls):
        # Se conectando com os bancos de dados
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


    def get_id(self, user) -> str:
        """
        Método responsável por retornar o  id do usuário
        """
        cursor_users = self.connection_users.cursor()
        command = f"SELECT id FROM login WHERE user=\"{user}\""
        cursor_users.execute(command)
        return str(cursor_users.fetchall()[0][0])


    def create_table_codeuser(cls, id_user):
        """
        Método responsável pela criação da tabela de acordo com o id do usuário, para assim termos a conexão
        da carteira com o seu respectivo dono
        """
        cursor_codes = cls.connection_codes.cursor()
        command = f"CREATE TABLE {'user_'+id_user}(codigo VARCHAR(255), tipo VARCHAR(255), empresa VARCHAR(255),"
        command += "indicador_01 VARCHAR(255), indicador_02 VARCHAR(255), indicador_03 VARCHAR(255), "
        command += "indicador_04 VARCHAR(255), indicador_05 VARCHAR(255),indicador_06 VARCHAR(255), PRIMARY KEY(codigo))"
        cursor_codes.execute(command)

    def verificacao_login(cls, user, password):
        """
        Método de verificação de login
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
        Método de registro de usuario, além de chamar a função create_table_codeuser()
        retorna None, caso exista o usuário no banco de dados
        retorna True, caso o registro seja bem sucedido
        retorna False, caso ocorra um erro no registro
        """
        command = f"SELECT user FROM login WHERE user=\"{user}\""
        cursor_users = cls.connection_users.cursor()
        cursor_users.execute(command)

        pesq = cursor_users.fetchall()

        if pesq:
            return None
        else:
            # Inserindo no banco action_stalker_users, na tabela login, apenas o usuário e a senha, já que o id é auto incrementado
            command = "INSERT INTO login(user, password) VALUES (%s, %s)"
            valor = (user, password)

        try:
            cursor_users.execute(command, valor)
            cls.connection_users.commit()

            # snippet responsável pela criação da tabela user_n de acordo com o respectivo id do usuário
            command = f"SELECT id FROM login WHERE user=\"{user}\""
            cursor_users.execute(command)
            id_user = str(cursor_users.fetchall()[0][0])
            cls.create_table_codeuser(id_user)  # Criando a tabela de códigos para o usuário em específico
            return True
        except:
            return False

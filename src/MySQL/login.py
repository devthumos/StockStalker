import pymysql as py

class Login:
    def __init__(cls):
        # Criando conexão
        cls.con = py.connect(
            host="localhost",
            user="root",
            password="",
            database="action_stalker"
            )


    """
    Função de verificação de login
    retorna None, caso as credenciais sejam inválidas
    retorna um conteúdo, caso as credenciais sejam válidas 
    """
    def verificacao_login(cls, user, password):
        command = f"SELECT user, password FROM login WHERE user=\"{user}\" and password=\"{password}\""
        cursor = cls.con.cursor()
        cursor.execute(command)

        pesq = cursor.fetchall()

        return pesq

    """
    Função de registro de login
    retorna None, caso exista o usuário no banco de dados
    retorna True, caso o registro seja bem sucedido
    retorna False, caso ocorra um erro no registro 
    retorna   
    """
    def registrar_login(cls, user, password):
        command = f"SELECT user FROM login WHERE user=\"{user}\""
        cursor = cls.con.cursor()
        cursor.execute(command)

        pesq = cursor.fetchall()

        if pesq:
            return None
        else:
            command = "INSERT INTO login(user, password) VALUES (%s, %s)"
            valor = (user, password)

            try:
                cursor.execute(command, valor)
                cls.con.commit()
                return True
            except:
                return False

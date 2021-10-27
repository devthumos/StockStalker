import pymysql as py
from src.Web_Scraping.statusinvest import Webscrapper


class RegistroMySQL:
    """
    Essa classe é responsável pela conexão com o banco de dados action_stalker_codes, pelo registro de códigos, update de código
    e remoção de códigos, além da listagem de códigos disponíveis na tabela do usuário
    """
    def __init__(self):
        # Se conectando com o banco
        try:
            self.connection_codes = py.connect(
                host="localhost",
                user="root",
                password="",
                database="ACTION_STALKER_CODES"
                )
        except:
            print("ERRO, Não Foi Possível Conectar ao Banco de Dados")

    def registrar_registros(self, codigo, indicadores, id_user):
        """
        Método de registro dos indicadores no banco de dados
        retorna False, caso já exista o código no banco de dados
        """
        cursor_codes = self.connection_codes.cursor()

        try:
            command = f"INSERT INTO {id_user}(codigo, tipo, empresa, indicador_01, indicador_02, indicador_03, indicador_04,"
            command += " indicador_05, indicador_06) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valor = (codigo, indicadores[1], indicadores[0][0], indicadores[0][1], indicadores[0][2], indicadores[0][3], indicadores[0][4], indicadores[0][5], indicadores[0][6])

            cursor_codes.execute(command, valor)
            self.connection_codes.commit()
        except:
             return False

    def list_elements(self, id_user):
        """
        Método que lista todos os elmentos da tabela de códigos do usuário, o user_n
        retorna None, caso não exista elementos no banco de dados
        retorna algum conteúdo, caso exista elementos no banco de dados
        """
        command = f"SELECT * FROM {id_user}"
        cursor_codes = self.connection_codes.cursor()
        cursor_codes.execute(command)

        elements = cursor_codes.fetchall()

        return elements

    def update_registro(self, id_user): # , indicadores
        """
        Método que atualiza os indicadores do código listados na tabela do usuário
        """
        object_webscraper = Webscrapper()
        command = f"SELECT * FROM {id_user}"
        cursor_codes = self.connection_codes.cursor()
        cursor_codes.execute(command)
        codes = cursor_codes.fetchall()

        for i in codes:
            indicadores = object_webscraper.main(i[0])
            command = f"UPDATE {id_user} SET tipo=\"{indicadores[1]}\", empresa=\"{indicadores[0][0]}\", indicador_01=\"{indicadores[0][1]}\", indicador_02=\"{indicadores[0][2]}\", indicador_03=\"{indicadores[0][3]}\", indicador_04=\"{indicadores[0][4]}\", indicador_05=\"{indicadores[0][5]}\", indicador_06=\"{indicadores[0][6]}\" WHERE codigo=\"{i[0]}\""
            cursor_codes.execute(command)

        self.connection_codes.commit()

    def delete_registro(self, id_user, codigo):
        """
        Método que dele o código da tabela user_n
        """
        command = f"DELETE FROM {id_user} WHERE codigo=\"{codigo}\""
        cursor_codes = self.connection_codes.cursor()
        cursor_codes.execute(command)
        self.connection_codes.commit()

"""
Área de testes
"""
# if __name__ == "__main__":
#     item = RegistroMySQL()
#     # item.update_registro("user_1")
#     item.delete_registro("user_1", "gogl34")

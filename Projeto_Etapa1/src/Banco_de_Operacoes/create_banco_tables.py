import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",

    )

cursor = connection.cursor()
cursor.execute("CREATE DATABASE ACTION_STALKER_OPERATIONS")

connection_operations = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="ACTION_STALKER_OPERATIONS"
)

cursor = connection_operations.cursor()

command = f"CREATE TABLE fundos_imobiliarios(codigo VARCHAR(255),"
command += "Empresa VARCHAR(255), Valor_Atual VARCHAR(255), Min_52_Semanas VARCHAR(255), "
command += "Max_52_Semanas VARCHAR(255), Dividend_Yield VARCHAR(255), Valorizacao_12M VARCHAR(255), PRIMARY KEY(codigo))"
cursor.execute(command)

command = f"CREATE TABLE bdrs(codigo VARCHAR(255),"
command += "Empresa VARCHAR(255), Valor_Atual VARCHAR(255), Min_52_Semanas VARCHAR(255), "
command += "Max_52_Semanas VARCHAR(255), Dividend_Yield VARCHAR(255), Valorizacao_12M VARCHAR(255), PRIMARY KEY(codigo))"
cursor.execute(command)

command = f"CREATE TABLE acao(codigo VARCHAR(255),"
command += "Empresa VARCHAR(255), Valor_Atual VARCHAR(255), Min_52_Semanas VARCHAR(255), "
command += "Max_52_Semanas VARCHAR(255), Dividend_Yield VARCHAR(255), Valorizacao_12M VARCHAR(255), PRIMARY KEY(codigo))"
cursor.execute(command)

command = f"CREATE TABLE fundos_de_investimento(codigo VARCHAR(255),"
command += "Empresa VARCHAR(255), Preco_da_Cota VARCHAR(255), Rentabilidade_12M VARCHAR(255), "
command += "Rentabilidade_24M VARCHAR(255), Volatilidade_6M VARCHAR(255), Indice_de_Sharpe_6M VARCHAR(255), "
command += "Patrimonio_Liquido VARCHAR(255), PRIMARY KEY(codigo))"
cursor.execute(command)

command = f"CREATE TABLE tesouro(codigo VARCHAR(255),"
command += "Valor_Unitario VARCHAR(255), Taxa_de_Rentabilidade VARCHAR(255), Min_52_Semanas VARCHAR(255), "
command += "Max_52_Semanas VARCHAR(255), Valorizacao_12M VARCHAR(255), PRIMARY KEY(codigo))"
cursor.execute(command)
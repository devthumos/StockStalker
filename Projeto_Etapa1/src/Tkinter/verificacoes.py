import re


class Verificacoes:


    def verificacao_usuario(self, string: str) -> bool:
        if len(string) < 4 or len(string) > 20:
            return False

        if re.search('r[^0-9a-z_]+', string, flags=re.I):
            return False
        else:
            return True


    def verificacao_senha(self, string: str) -> bool:
        if len(string) < 4 or len(string) > 20:
            return False

        if re.search('r[^0-9a-z_\$#%&\*()+\-.!@{}\[\]?=]+', string, flags=re.I):
            return False
        else:
            return True


    def verificacao_codigo(self, string: str) -> bool:
        if len(string) > 50 or string == " ":
            return False

        if re.search(r'[^\w\d" "]', string, flags=re.I):
            return False
        else:
            return True


        # TESTES
item = Verificacoes()

    # Validação de Usuário
# if item.verificacao_usuario(input()):
#     print("String Válida")
# else:
#     print("String Não Válida")

    # Validação de Senha
# if item.verificacao_senha(input()):
#     print("String Válida")
# else:
#     print("String Não Válida")

    # Validação de Código
if item.verificacao_codigo(input()):
    print("String Válida")
else:
    print("String Não Válida")


from login import LoginMySQL

if __name__ == "__main__":
    log_object = LoginMySQL()

            # TESTE
    while True:
        opcao = input("Insira uma Opção:\n[1] Logar\n[2] Registrar\n[3] Sair\n")
        print(end="\n")

        if opcao == "1":

            user = input("Insira o Usuário: ")
            passwd = input("Insira a Senha: ")

            pesq = log_object.verificacao_login(user, passwd)
            if pesq:
                print("ACESSO PERMITIDO")
            else:
                print("ACESSO NEGADO")
        elif opcao == "2":

            user = input("Insira o Usuário: ")
            passwd = input("Insira a Senha: ")

            result = log_object.registrar_login(user, passwd)

            if result == True:
                print(f"USUÁRIO {user} REGISTRADO COM SUCESSO")
            elif result == None:
                print(f"USUÁRIO {user} JÁ EXISTE\nINSIRA OUTRO USUÁRIO")
            else:
                print(f"ERRO, NÃO FOI POSSÍVEL REGISTRAR O USUÁRIO {user}")
        elif opcao == "3":
            break
        else:
            print("Insira uma opção válida")

from registro import RegistroMySQL

if __name__ == "__main__":
    registro_object = RegistroMySQL()

            # TESTE
    while True:
        opcao = input("Insira uma Opção:\n[1] Registrar Bolsas\n[2] Listar Bolsas\n[3] Sair\n")
        print(end="\n")

        if opcao == "1":

            code = input("Insira o Código: ")
            type = input("Insira o Tipo: ")

            pesq = registro_object.registrar_registros(code, type)
            if pesq == None:
                print("CÓGIDO JÁ EXISTE, INSIRA OUTRO PARA O REGISTRO")
            elif pesq == True:
                print("REGISTRO BEM SUCEDIDO")
            else:
                print("ERRO, NÃO FOI POSSÍVEL REGISTRAR")
        elif opcao == "2":
            result = registro_object.list_elements()

            for x in result:
                print(x)
        elif opcao == "3":
            break
        else:
            print("Insira uma opção válida")
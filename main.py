def main():
    while True:
        print("\nBoas vindas ao nosso sistema:")
        print("1 - Inserir usuário")
        print("2 - Excluir usuário")
        print("3 - Atualizar usuário")
        print("4 - Informações de um usuário")
        print("5 - Informações de todos os usuários")
        print("6 - Sair")

        option = input("Escolha uma opção: ")
        if option == '1':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")

        elif option == '6':
            print("Saindo...")
            break

        else:
            print("Opção Inválida.")


if __name__ == "__main__":
    main()
import loadJSON
import repository


def main():
    contacts, id = loadJSON.load()
    while True:
        menu_str = """
\nBoas vindas ao nosso sistema:

1 - Inserir usuário
2 - Excluir usuário
3 - Atualizar usuário
4 - Informações de um usuário
5 - Informações de todos os usuários
6 - Sair\n
"""
        print(menu_str)

        option = input("Escolha uma opção: ")
        if option == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            address = input("Address: ")

            repository.add_user(name, id, contacts, phone, address)

        elif option == '2':
            while True:
                idDelete = input("Insira o ID do usuário que deseja excluir: ")
                if idDelete not in contacts:
                    print("Usuário não encontrado!")
                else:
                    repository.delete_user(idDelete, contacts)
                    break
        elif option == '6':
            print("Saindo...")
            break

        else:
            print("Opção Inválida.")


if __name__ == "__main__":
    main()

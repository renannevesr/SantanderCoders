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
            num_users = int(input("Quantos usuários deseja adicionar? "))
            for num in range(num_users):
                name = input("Name: ")
                phone = input("Phone: ")
                address = input("Address: ")
                id = repository.add_user(name, id, contacts, phone, address)

        elif option == '2':
            contacts, id = loadJSON.load()
            while True:
                idDelete = input("Insira o ID do usuário que deseja excluir: ")
                if idDelete not in contacts:
                    print("Usuário não encontrado!")
                else:
                    repository.delete_user(idDelete, contacts)
                    break

        elif option == '3':
            contacts, id = loadJSON.load()
            while True:
                idToUpdate = input("Insira o ID do usuário: ")
                if idToUpdate not in contacts:
                    print("Usuário não encontrado!")
                else:
                    print("Qual informação deseja alterar?")
                    print("1 - Nome")
                    print("2 - Telefone")
                    print("3 - Endereço")
                    field = input()

                    if field not in ['1', '2', '3']:
                        print("Opção inválida.")
                    else:
                        new_value = input(
                            f"Insira o novo valor para a opção {field}: ")
                        repository.update_user(
                            idToUpdate, field, new_value, contacts)
                        break

        elif option == '4':
            contacts, id = loadJSON.load()
            while True:
                idToShow = input("Insira o ID do usuário: ")
                if idToShow not in contacts:
                    print("Usuário não encontrado!")
                else:
                    repository.show_user(idToShow, contacts)
                    break

        elif option == '5':
            contacts, id = loadJSON.load()
            repository.index(contacts)

        elif option == '6':
            print("Saindo...")
            break

        else:
            print("Opção Inválida.")


if __name__ == "__main__":
    main()

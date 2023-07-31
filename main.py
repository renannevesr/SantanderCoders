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
            contacts, ids = loadJSON.load()
            ids_to_delete = input(
                "Insira os IDs dos usuários que deseja excluir (separados por vírgula): ").split(',')
            users_not_found = []
            for idDelete in ids_to_delete:
                idDelete = idDelete.strip()  # Remover espaços em branco extras, se houver
                if idDelete not in contacts:
                    users_not_found.append(idDelete)
                else:
                    repository.delete_user(idDelete, contacts)

            if users_not_found:
                print("Usuários não encontrados:", ", ".join(users_not_found))
            else:
                print("Usuários excluídos com sucesso!")

        elif option == '3':
            contacts, _ = loadJSON.load()
            ids_to_update = []

            while True:
                id_to_update = input(
                    "Insira o ID do usuário que deseja editar (ou digite 0 para finalizar): ")
                if id_to_update == '0':
                    break

                if id_to_update not in contacts:
                    print(f"Usuário com ID {id_to_update} não encontrado!")
                else:
                    ids_to_update.append(id_to_update)

            if not ids_to_update:
                print("Nenhum ID válido foi inserido.")
            else:
                for id_to_update in ids_to_update:
                    print("ID do usuário a ser editado:", id_to_update)
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
                            id_to_update, field, new_value, contacts)

        elif option == '4':
            contacts, _ = loadJSON.load()
            while True:
                id_to_show = input(
                    "Insira os IDs dos usuários separados por vígulas (ou vazio para sair): ")
                if not id_to_show:
                    break
                else:
                    id_list = id_to_show.split(',')
                    repository.show_user(*id_list, contacts=contacts)

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

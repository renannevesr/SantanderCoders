import loadJSON


def add_user(name, id, contacts, phone="Não Informado", address="Não Informado"):

    for user_key, user_data in contacts.items():
        if user_data["Nome"] == name and user_data["Telefone"] == phone and user_data["Endereço"] == address and not user_data["Status"]:
            user_data["Status"] = True
            break
    else:
        id += 1
        new_user = {
            "Status": True,
            "Nome": name,
            "Telefone": phone,
            "Endereço": address,
            "ID": id
        }
        contacts[id] = new_user
    loadJSON.save(contacts)


def delete_user(ids_to_delete, contacts):
    for user_key, user_data in contacts.items():
        if user_data["ID"] in ids_to_delete:
            user_data["Status"] = False

    loadJSON.save(contacts)


def update_user(id_to_update, field, new_value, contacts):
    if id_to_update in contacts:
        user_data = contacts[id_to_update]
        if field == '1':
            user_data["Nome"] = new_value
        elif field == '2':
            user_data["Telefone"] = new_value
        elif field == '3':
            user_data["Endereço"] = new_value
        else:
            print("Opção inválida.")
    else:
        print("Usuário não encontrado.")

    loadJSON.save(contacts)


def show_user(id, contacts):
    if id in contacts:
        user_data = contacts[id]
        print(f"Nome: {user_data['Nome']}")
        print(f"Telefone: {user_data['Telefone']}")
        print(f"Endereço: {user_data['Endereço']}")
    else:
        print("Usuário não encontrado.")


def index(contacts):
    for user_data in contacts.values():
        if user_data["Status"]:
            print(f"ID: {user_data['ID']}")
            print(f"Nome: {user_data['Nome']}")
            print(f"Telefone: {user_data['Telefone']}")
            print(f"Endereço: {user_data['Endereço']}")
            print()

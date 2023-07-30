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
    return contacts

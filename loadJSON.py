import json


def load():
    try:
        with open('projetoModuloII.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    new = {}
    id = 0
    for chave, subdicionario in contacts.items():
        subdicionario["ID"] = chave
        new[chave] = subdicionario
        id += 1
    return new, id


def save(data):
    try:
        with open("projetoModuloII.json", "w") as file:
            json.dump(data, file)
        print("Dados salvos com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

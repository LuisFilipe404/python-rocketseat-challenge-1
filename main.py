contacts = []


def create_contact():
    name = input("Digite o nome do contato: ")
    phone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")

    contact = {"name": name, "phone": phone, "email": email, "favorite": False}

    contacts.append(contact)

    return


def list_contacts():
    for indice, contato in enumerate(contacts):

        favorite = "Sim" if contato["favorite"] else "Não"

        print("\n")
        print("--------------------")
        print("ID: ", indice)
        print("Nome: ", contato["name"])
        print("Telefone: ", contato["phone"])
        print("Email: ", contato["email"])
        print("Favorito: ", favorite)
        print("--------------------")
        print("\n")

    return


def update_contact():
    list_contacts()

    contact_id = int(input("Digite o ID do contato que deseja editar: "))

    contact = contacts[contact_id]

    while True:
        print("\nEscolha uma opção:\n")
        print("1. Editar nome")
        print("2. Editar telefone")
        print("3. Editar email")
        print("4. Finalizar edição")

        option = input("\nDigite o número da opção desejada: ")

        if option == "1":
            contact["name"] = input("Digite o novo nome: ")
        elif option == "2":
            contact["phone"] = input("Digite o novo telefone: ")
        elif option == "3":
            contact["email"] = input("Digite o novo email: ")
        elif option == "4":
            break


def favorite_contact():
    list_contacts()

    contact_id = int(input("Digite o ID do contato que deseja favoritar: "))

    contact = contacts[contact_id]

    contact["favorite"] = True

    return


def list_favorite_contacts():
    for contato in contacts:
        if len(contacts) == 0:
            print("Nenhum contato favoritado.")
        else:
            if contato["favorite"]:
                print("--------------------")
                print("Nome: ", contato["name"])
                print("Telefone: ", contato["phone"])
                print("Email: ", contato["email"])
                print("Favorito:", "Sim")
                print("--------------------")


def remove_contact():
    list_contacts()

    contact_id = int(input("Digite o ID do contato que deseja remover: "))

    contacts.pop(contact_id)

    return


while True:
    print("\nEscolha uma opção:\n")
    print("1. Adicionar um contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Listar contatos favoritos")
    print("6. Remover contato")
    print("7. Sair")

    option = input("\nDigite o número da opção desejada: ")

    if option == "1":
        create_contact()
    elif option == "2":
        list_contacts()
    elif option == "3":
        update_contact()
    elif option == "4":
        favorite_contact()
    elif option == "5":
        list_favorite_contacts()
    elif option == "6":
        remove_contact()
    elif option == "7":
        break
    else:
        print("Opção inválida")

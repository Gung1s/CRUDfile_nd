from CRUD_fun import *

authors = load_data()
print()

while True:
    print_info()
    print()
    print("Įvesk norimą komandą:")
    choise = input()

    match choise:
        case "1":
            print_data(authors)
            print()
        case "2":
            create_data(authors)
        case "3":
            edit_data(authors)
        case "4":
            delete_data(authors)
        case "5":
            print("Programa uždaroma.")
            break
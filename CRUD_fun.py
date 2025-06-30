import csv


def print_info():
    print("1. Parodyti autorių sąrašą")
    print("2. Įtraukti naują autorių")
    print("3. Redaguoti autorių")
    print("4. Ištrinti autorių")
    print("5. Išeiti iš programos")

def load_data():
    with open("english_authors_list.csv", mode="r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def print_data(authors):
    print()
    print("Autoriai:")
    for a in authors:
        print(f"{a["id"]}. Vardas: {a["name"]}, Pavardė: {a["surname"]}")

def save_data(authors):
    with open("english_authors_list.csv", mode="w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "surname"])
        writer.writeheader()
        writer.writerows(authors)

def create_data(authors):
    print("Įtraukti naują autorių")
    print("Vardas")
    name = input()
    print("Pavardė")
    surname = input()
    new_id = str(int(authors[-1]["id"]) + 1) if len(authors) > 0 else 1
    authors.append({"id": new_id, "name": name, "surname": surname})
    save_data(authors)

def edit_data(authors):
    print(f"Redaguoti esamus autorius.",
          f"Įveskite id, kurį autorių norite redaguoti")
    id = input()
    for a in authors:
        if id == str(a["id"]):
            print(f"{a["id"]}. Vardas: {a["name"]}, Pavardė: {a["surname"]}")
            print("Įveskite vardą:")
            a["name"] = input()
            print("Įveskite pavardę:")
            a["surname"] = input()
            break
    save_data(authors)


def delete_data(authors):
    print(f"Autoriaus pašalinimas iš sąrašo.",
          f"Pasirinkite ID kurį, norite pašalinti")
    id = input()
    for a in authors:
        if id == str(a["id"]):
            print(f"Pašalintas:",
                  f"{a["id"]}. Vardas: {a["name"]}, Pavardė: {a["surname"]}")
            del authors[authors.index(a)]
            print()
    save_data(authors)

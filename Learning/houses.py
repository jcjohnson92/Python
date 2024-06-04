students = [
    {"name": "Hermione", "house":"Grffindor"},
    {"name": "Harry", "house":"Grffindor"},
    {"name": "Ron", "house":"Grffindor"},
    {"name": "Draco", "house":"Slytherin"},
    {"name": "Padma", "house":"Ravenclaw"},
]


def get_houses():
    houses = list()
    for student in students:
        if student["house"] not in houses:
            houses.append(student["house"])

    for house in sorted(houses):
        print(house)


def get_set_houses():
    houses=set()
    for student in students:
        houses.add(student["house"])

    for house in houses:
        print(house)

print("Set version")
get_set_houses()

print("\n\n\nList version ")
get_houses()
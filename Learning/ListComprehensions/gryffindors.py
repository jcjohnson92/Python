# students = [
#     {"name": "Hermione", "house":"Grffindor"},
#     {"name": "Harry", "house":"Grffindor"},
#     {"name": "Ron", "house":"Grffindor"},
#     {"name": "Draco", "house":"Slytherin"},
#     {"name": "Padma", "house":"Ravenclaw"},
# ]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Grffindor"
# ]
# print(*gryffindors, sep='\n')

# def is_gryffindors(s):
#     return s['house'] == "Grffindor"

# gryffindors=filter(is_gryffindors,students)

# for gryffindor in sorted(gryffindors, key=lambda s: s['name']):
#     print(gryffindor['name'])


students = ["Hermione", "Harry", "Ron"]

gryffidors = [{"name":student,"house":"Gryffindors"} for student in students]
print(gryffidors)
""" Zadanie 3 – Porównanie imion """

first_name = input("podaj pierwsze imię: ")
second_name = input("Podaj drugie imię: ")

if first_name == second_name:
    print("Takie same")
else:
    print("Różne")


""" dla imion lepiej uczynic porównanie nieczułym na wielkość liter"""

print("Porównanie bez względu na wielkość liter")


if first_name.lower() == second_name.lower():
    print("Takie same")
else:
    print("Różne")



""" Zadanie 8 – Wiek użytkownika """

import datetime

now = datetime.datetime.now()
name = input("Podaj swoje imię: ")
year = input("Podaj rok swojego urodzenia: ")
year = int(year)
age = now.year - year

print(f"Użytkownik: {name} jest w wieku {age} lat.")

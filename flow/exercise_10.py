""" Zadanie 10 – Tabliczka mnożenia """

number = 0

while number < 1 or number > 10:
    number = input("Podaj liczbę w zakresie 1 .. 10 ")
    number = int(number)

for i in range (1, 11):
    print(f"{i} * {number} = {i * number}")


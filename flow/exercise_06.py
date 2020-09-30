""" Zadanie 6 – Suma liczb """

number = 111
while number < 0 or number > 100:
    number = input("Podaj liczbę z zakresu 0 .. 100: ")
    number = int(number)

print("\nPętla while:")

i = 0
suma = 0

while i < number + 1:
    suma += i
    i += 1

print(f"Suma liczb od 0 do {number} to: {suma}")

print("\nRange i sum:")

print(f"Suma liczb od 0 do {number} używając sum i range: "
      f"{sum(range(number + 1))}")

""" Zadanie 7 – Średnia """

n = 0
numbers = []
numbers_as_string = []
separator = " "

while n < 1:
    n = input("Ile liczb będzie wprowadzonych? ")
    n = int(n)

for i in range(n):
    tmp = input(f"Podaj {i + 1} liczbę: ")
    numbers_as_string.append(tmp)
    numbers.append(int(tmp))

sum_numbers = sum(numbers)
average = sum_numbers / n
tmp = "Suma" if sum_numbers > average else "Średnia"

print(f"Wprowadzone liczby: {separator.join(numbers_as_string)}")
print(f"suma: {sum_numbers}, średnia: {average}")
print(f"{tmp} jest większa!")

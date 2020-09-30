""" Zadanie 11 – Fizzbuzz """

for i in range(1, 101):
    # print(f"l: {i}")
    fizz = "Fizz" if not i % 3 else ""  # tak, bo dla liczb podzielnych
    # wynikiem modulo jest 0, a to jest False
    buzz = "Buzz" if not i % 5 else ""
    if fizz or buzz:
        print(f"{fizz}{buzz}")
    else:
        print(i)

""" Zadanie 5 – Równania kwadratowe """

print("Równanie w postaci a*x**2 + b*x + c == 0")


a = 0
while a == 0:
    a = input("Podaj a, a nie może być równe 0: ")
    a = float(a)

b = input("Podaj b: ")
b = float(b)
c = input("Podaj c: ")
c = float(c)

delta = b**2 - 4 * a * c


if delta > 0:
    x_1 = round((-1 * b - delta**0.5) / (2* a), 4)
    x_2 = round((-1 * b + delta**0.5) / (2* a), 4)
    out_string = f"x_1 = {x_1}\nx_2 = {x_2}"
elif delta == 0:
    x_1 = x_2 = round((-1 * b) / (2 * a), 4)
    out_string = f"x_1 = x_2 = {x_1}"
else:
    x_1 = X_2 = None
    out_string = "Równanie nie ma pierwiastków"

print("Pierwiastki równania kwadratowego:")
print(out_string)


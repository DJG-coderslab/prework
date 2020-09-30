""" Zadanie 8 – Porównywanie napisów """

kot = "kot"
pies = "pies"

print(f"Pies < kot? {pies > kot}")

"""
Porównanie stringów następuje od pierwszych pozycji stringów, a porównywany 
jest kod znaku. Dla kot pierwszym znakiem jest 'k' o kodzie 107, a dla pies
pierwszym znakiem jest 'p' o kodzie 112. Jeśli pierwsze znaki sa takie same, 
do porównania brany jest kolejny znak.
"""
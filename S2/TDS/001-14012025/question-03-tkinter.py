from random import randint
from tkinter import messagebox
print("Bienvenue dans notre jeu \n\n")

while True:
    nombre = randint(1, 100)
    essai = 0
    while True:
        essai += 1
        proposition = int(input("Entrez un nombre entre 1 et 100: "))
        if proposition < nombre:
            print("Trop petit")
        elif proposition > nombre:
            print("Trop grand")
        else:
            print(f"Bravo, vous avez trouvé le nombre en {essai} essais")
            break
    if messagebox.askyesno("Rejouer", "Vouslez-vous arrêtez ?"):
        break
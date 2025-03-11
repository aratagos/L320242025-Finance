chaine1 = "Bonjour"
chaine2 = "tout le monde"

lettre_commune = tuple(char for char in chaine1 if char in chaine2)

print(lettre_commune)
lettre_commune = tuple(char for car in chaine1 for char in chaine2 if car == char)

l = []
for car in chaine1:
    for char in chaine2:
        if car == char:
            l.append(car)

l = tuple(l)
print(l)


print(lettre_commune)
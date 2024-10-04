n = int(input('Entrez la taille du damier : '))

for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            print('X', end='')
        else:
            print('O', end='')
    print()

damier = []
for i in range(n):
    ligne = []
    for j in range(n):
        if (i+j) % 2 == 0:
            ligne.append('X')
        else:
            ligne.append('O')
    damier.append(ligne)

liste_chaine = ['banane', 'pomme', 'poire', 'fraise', 'framboise', 'cerise', 'abricot', 'peche', 'raisin', 'orange']

remplacement_voyelle = [''.join(['*' if char in 'aeiou' else char for char in word]) for word in liste_chaine]

print(remplacement_voyelle)
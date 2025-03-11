phrase = "This is a sample sentence"
longueur_mots = [len(mot) for mot in phrase.split()]
print(longueur_mots)
print('*'*50)
phrase = "This is a sample sentence."
longueur_mots = [len(mot) for mot in phrase.split()]
print(longueur_mots)
print('*'*50)
phrase = "This is a sample sentence."
longueur_mots = [len(mot.replace('.','')) for mot in phrase.split()]
print(longueur_mots)

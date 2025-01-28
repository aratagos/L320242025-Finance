phrase = "Portez ce vieux whisky au juge blond qui fume"

def est_pangramme(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")

    lettres = ''
    for car in phrase:
        if car not in lettres:
            lettres += car

    return len(lettres) == 26

print(est_pangramme(phrase))

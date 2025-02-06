from comptes import comptes

def synthese_familles(**comptes_a_synthetiser):
    synthese = {}
    for compte in comptes_a_synthetiser.values():
        if  compte["nom"]  not in synthese:
            synthese[compte["nom"]] = compte.get("epargne", 0)
        else:
            synthese[compte["nom"]] += compte.get("epargne", 0)
    pauvre = min(synthese, key=synthese.get)
    riche = max(synthese, key=synthese.get)
    
    return (pauvre, synthese[pauvre]), (riche, synthese[riche])


print(synthese_familles(**comptes))
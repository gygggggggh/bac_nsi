def moyenne(notes): # ponderees
    """Calcule la moyenne ponderee des notes
    notes est une liste de listes de deux elements
    le premier element est la note
    le second element est le coefficient
    """
    somme = 0
    poids = 0
    for note in notes:
        somme += note[0] * note[1]
        poids += note[1]
    return somme / poids

print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
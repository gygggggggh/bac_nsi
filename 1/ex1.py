def verifie(tab):
    minimun = tab[0]
    for i in tab:
        if minimun > i :
            return False
        else:
            minimun = i
    return True

print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))
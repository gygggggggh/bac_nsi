def indices_maxi(tab):
    maxi = tab[0]
    c = []
    for i in range(len(tab)):
        if tab[i] > maxi :
            maxi = tab[i]
    for i in range(len(tab)):
        if tab[i] == maxi :
            c.append(i)
    return (maxi,c)

print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))
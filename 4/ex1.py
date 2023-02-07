def a_doubloons(tab):
    for i in range(len(tab)):
        if tab[i] in tab[i+1:]:
            return True
    return False

print(a_doubloons([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(a_doubloons([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))
print(a_doubloons([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))
print(a_doubloons([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1]))
print(a_doubloons([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]))

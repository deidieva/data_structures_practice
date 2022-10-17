

def sum_list(listik):
    sum = 0
    if listik:
        first_element = listik[0]
        listik.pop(0)
        sum = first_element + sum_list(listik)

    return sum


listo = [3, 2, 1]
print(sum_list(listo))

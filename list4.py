def last_to_first(lst):
    if len(lst) <= 1:
        return lst
    last_element = lst.pop()
    lst.insert(0, last_element)
    return lst
moy_list = [1,10,24,5]
resultat = last_to_first(moy_list)
print(resultat)
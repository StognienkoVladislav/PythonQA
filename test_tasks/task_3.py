
def same_structure_as(np1, np2):
    if len(np1) != len(np2):
        return False

    for lst1, lst2 in zip(np1, np2):
        if type(lst1) != type(lst2):
            return False

        # т.к. типы 2 элементов одинаковые, можно сравнить только 1
        elif type(lst1) is list:
            return same_structure_as(lst1, lst2)
    return True

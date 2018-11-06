
def same_structure_as(structure_1, structure_2):
    if len(structure_1) != len(structure_2):
        return False

    for internal_1, internal_2 in zip(structure_1, structure_2):
        if type(internal_1) != type(internal_2):
            return False

        # т.к. типы 2 элементов одинаковые, можно сравнить только 1
        elif type(internal_1) is list:
            return same_structure_as(internal_1, internal_2)
    return True

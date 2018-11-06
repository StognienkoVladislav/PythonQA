
def binary_count(number):
    str_from_numb = "{0:b}".format(number)
    return list(map(str, str(str_from_numb))).count('1')

def get_item_at(p1: list, p2: int) -> int:
    if (p2 >= 0) and p2 < len(p1):
        return p1[p2]
    else:
        return -1

def get_first_digit(p1: str) -> int:
    for char in p1:
        if char.isdigit():
            return char
    return ""

def contains_boolean(p1: list) -> bool:
    for item in p1:
        if type(item) == type(True) or type(item) == type(False):
            return True
    return False

def shorter_list(p1: list, p2: list) -> list:
    empty_list = []
    if len(p1) < len(p2):
        return p1
    elif len(p1) == len(p2):
        return empty_list
    else:
        return p2

def first_two_items(p1: list) -> list:
    empty_list = []
    if len(p1) > 1:
        return p1[0:2]
    elif len(p1) == 1:
        return p1
    else:
        return empty_list

def last_n_items(p1: list, p2: int) -> list:
    return p1[-p2:]

def shortest_word(p1: list) -> str:
    if len(p1) == 0:
        return ""
    else:
        smallest_string = p1[0]
        x = 1
        while x < len(p1):
            if p1[x] < p1[x-1]:
                smallest_string = p1[x]
            x += 1
    return smallest_string

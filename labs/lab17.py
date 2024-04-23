
def index_to_val(plist: list, p1: int) -> str:
    if p1 >= 0 and p1 < len(plist):
        val = plist[p1]
        return str(p1) +" -> " + str(val)
    else:
        return ""


def val_to_index(plist: list, p1) -> str:
    if p1 in plist:
        curr_index = plist.index(p1)
        return str(curr_index) + " -> " + str(p1)
    else:
        return ""

def list_pretty_print(plist: list) -> str:
    my_string = ""
    for value in plist:
        curr_index = plist.index(value)
        my_string += str(curr_index) + " -> " + str(value) + "\n"
    my_string = my_string.strip()
    return my_string

def list_to_dict(plist: list) -> dict:
    d1 = {}
    for index in range(len(plist)):
        d1[index] = plist[index]
    return d1

def two_lists_to_dict(p1: list, p2: list):
    d1 = {}
    if len(p1) != len(p2):
        return d1
    else:
        for index in range(len(p1)):
            key = p1[index]
            val = p2[index]
            d1[key] = val
        return d1

'''

6. Implement the function two_smallest_ints which

takes one input parameter plist
plist  is a list of ints, all between 0 and 100, has no duplicates and is never empty
returns a list with the two smallest ints in plist
Your code may modify plist
'''

def filter_strings(plist: list, pstr: str) -> list:
    list2 = []
    for word in plist:
        if word.startswith(pstr):
            list2.append(word)
    return list2


def average_list(plist: list) -> int:
    total = 0
    if len(plist) == 0:
        return 0
    else:
        for num in plist:
            total = total + num
        average = total / len(plist)
    return average

def first_name_first(p1: str) -> str:
    first_last = p1.split(",")
    first = first_last[1]
    name = first[1::] + " " + first_last[0]
    return name

def last_name_first(p1: str) -> str:
    name = ""
    list_name = p1.split(" ")
    if len(list_name) == 2:
        name = list_name[1] + ", " + list_name[0]
    elif len(list_name) == 3:
        name = list_name[2] + ", " + list_name[0] + " " + list_name[1]
    return name

def find_min(plist: list) -> int:
    smallest = plist[0]
    for val in plist:
        if val < smallest:
            smallest = val
    return smallest

def two_smallest_ints(plist: list) -> list:
    smallest1 = plist[0]
    for val in plist:
        if val < smallest1:
            smallest1 = val
    list2 = plist
    list2.remove(smallest1)

    smallest2 = list2[0]
    for val in list2:
        if val < smallest2:
            smallest2 = val
    list3 = []
    list3.append(smallest1)
    list3.append(smallest2)
    return list3
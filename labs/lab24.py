'''1. Implement the function string_to_dict which

takes one input parameter p1 which is a str
p1 is a string representation of a list
each item in the list is a two item list
each two item list is a name followed by a score
returns a dictionary with an item for each two item list, with the value an int'''
def string_to_dict(p1: str) -> dict:
    d1 = {}
    myVals = p1.split("],")
    print(myVals)

    for val in myVals:
        val = val.replace("[", "")
        val = val.replace("]", "")
        val = val.strip()
        key, val = val.split(", ")
        val = int(val)
        d1[key] = val
    print(d1)
    return d1

'''2. Implement the function list_of_lists_to_dict which

takes one input parameter p1 which is a list of lists
each item in p1 is a list which has at least two items a name and at least one score
returns a dictionary with names as keys and list of scores as values'''
def list_of_lists_to_dict(p1: list) -> dict:
    print(p1)
    d1 = {}
    for list in p1:
        key = list[0]
        newList = list[1:]
        val = newList
        d1[key] = val

    return d1

'''3. Implement the function union which

takes two input parameters d1 and d2, both dictionaries
both d1 and d2 have string keys and int values
returns a dictionary with string keys and list values, including any key that is in either d1 or d2 or both'''
def union(d1: dict, d2: dict) -> dict:
    d3 = {}
    for key,val in d1.items():
        d3[key] = [val]
    print(d3)
    for key,val in d2.items():
        if key in d3.keys():
            d3[key].append(val)
        else:
            d3[key] = [val]
    return d3
    print(d3)

'''4. Implement the function intersection which

takes two input parameters d1 and d2, both dictionaries
both d1 and d2 have string keys and int values
returns a dictionary with string keys and list values, including any key that is in both d1 and d2'''
def intersection(d1: dict, d2: dict) -> dict:
    d3 = {}
    for key1, val1 in d1.items():
        for key2, val2 in d2.items():
            if key1 == key2:
                d3[key1] = []
                d3[key1].append(val1)
                d3[key1].append(val2)
    return d3
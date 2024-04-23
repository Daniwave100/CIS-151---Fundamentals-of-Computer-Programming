
def combo(string_param1: str, string_param2: str) -> str:
    if len(string_param1) > len(string_param2):
        return string_param1 + string_param2 + string_param1
    elif len(string_param2) > len(string_param1):
        return string_param2 + string_param1 + string_param2
    elif len(string_param1) == len(string_param2):
        return "equal"

def convert_string_to_list(string_param: str) -> list:
    list2 = []
    new_string = string_param[1:-1]
    new_string = new_string.strip()
    new_list = new_string.split(",")
    for val in new_list:
        new_val = val.strip(" ")
        list2.append(new_val)
    return list2 # slice or replace method

def convert_string_to_list2(string_param: str) -> int:
    list2 = []
    new_string = string_param[1:-1]
    new_string = new_string.strip()
    new_list = new_string.split(",")
    for val in new_list:
        new_val = val.strip(" ")
        list2.append(int(new_val))
    return list2

def merge_wo_dupes(p1: list, p2: list) -> list:
    result = []
    big_list = p1 + p2
    for val in big_list:
        if val not in result:
            result.append(val)
    return result

def intersection(p1: list, p2: list) -> list:
    new_list = []
    for val in p1:
        if val in p2:
            new_list.append(val)
    return new_list
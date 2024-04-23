
def is_vowel(param: str) -> bool: # function returns True if parameter letter is a vowel. if it is in "aeiou"
    if (len(param) == 1):
        if param in "aeiou":
            return True
    return False

def filter_vowels(p1: str) -> str:
    result = ""
    for char in p1:
        if is_vowel(char):
            result += char
    return result

def contains(plist: list, p2: str) -> bool:
    for item in plist:
        if item == p2:
            return True
    return False
    # if p2 in plist:
    #     return True
    # else:
    #     return False

def index_of(plist: list, p2: str) -> bool:
    for index in range(len(plist)):
        if p2 == plist[index]:
            return index
    return -1
    # if p2 in plist:
    #     return plist.index(p2)
    # else:
    #     return -1

def get_login(first_name: str, last_name: str) -> str:
    result = ""
    result = first_name[0:1:1]
    result += last_name[0:5]
    return result

def get_padded_login(first_name: str, last_name: str) -> str:
    result = first_name[0] + last_name[:5]
    if len(result) < 6:
        while len(result) < 6:
            result += "0"
        return result
    else:
        return result

def extract_name(p1: str) -> str:
        result = p1.split(":")
        if len(result) > 1:
            return result[1]
        else:
            return ""

def extract_full_name(p1: str) -> str:
    items = p1.split(",")
    first_name = ""
    last_name = ""

    for item in items:
        key, value = item.split(":")
        if key == "first_name":
            first_name = value
        elif key == "last_name":
            last_name = value

    full_name = first_name + " " + last_name
    return full_name




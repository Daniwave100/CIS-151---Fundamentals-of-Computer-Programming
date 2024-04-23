
def last_name_score(p1) -> str:
    new_list = p1.split(" ")
    new_word = new_list[1] + " " + new_list[2]
    new_word = new_word.replace(":", "")
    return new_word

def list_multiples_3(plist: list) -> list:
    multiples_3 = []
    for num in plist:
        if num % 3 == 0:
            multiples_3.append(num)
    return multiples_3

def string_before_ints(plist: list) -> list:
    string_list = []
    int_list = []
    total_list = []
    for val in plist:
        if type(val) == str:
            string_list.append(val)
        else:
            int_list.append(val)
    total_list = string_list + int_list
    return total_list

def state_abbreviation(p1: str) -> str:
    sentence = p1.split(" ")
    if len(sentence) == 1:
        return sentence[0][0:2].upper()
    else:
        return sentence[0][0:1] + sentence[1][0:1]
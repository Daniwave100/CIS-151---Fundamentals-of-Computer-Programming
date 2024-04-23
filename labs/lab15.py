

def extract_lab_number(p1: str, p2: str) -> str:
    d1 = {}
    l1 = p1.split(", ")
    for token in l1:
        if p2 in token:
            key, val = token.split(": ")
            return val
    return ""



    #     key,val = token.split(": ")
    #     key = key.replace("'", "")
    #     val = int(val)
    #     d1[key] = val
    #
    # if d1[p2] not in d1:
    #     return ""
    # else:
    #     return d1[p2]

def list_of_words(plist: list) -> list:
    list2 = []
    for string in plist:
        new_list = string.split(" ")
        if len(new_list) > 1:
            continue
        else:
            list2.append(string)
    return list2


def reorder_words_sentences(plist: list) -> list:
    words = []
    sentences = []
    final_list = []
    for item in plist:
        list2 = item.split(" ")
        if len(list2) > 1:
            sentences.append(item)
        else:
            words.append(item)
    final_list = words + sentences
    return final_list

def address_from_components(plist: list) -> str:
    sentence = ""
    new_list = []
    for item in plist:
        if type(item) == int:
            item = str(item)
            new_list.append(item)
        else:
            new_list.append(item)

    for item in new_list:
        sentence += item + " "

    sentence = sentence.rstrip()
    return sentence

def item_word_count(plist: list, p2: int) -> str:
    for sentence in plist:
        new_list = sentence.split(" ")
        if len(new_list) == p2:
            return sentence
    return ""


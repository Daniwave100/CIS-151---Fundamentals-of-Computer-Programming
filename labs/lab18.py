
def two_lists_to_dict(p1: list, p2: list) -> dict:
    d1 = {}
    if len(p1) < len(p2):
        for index in range(len(p1)):
            key = p1[index]
            val = p2[index]
            d1[key] = val
    else:
        for index in range(len(p1)):
            key = p1[index]
            if index < len(p2):
                val = p2[index]
            else:
                val = None
            d1[key] = val
    return d1


def dict_from_file(fname: str) -> dict:
    d1 = {}
    with open(fname) as fh:
        lines = fh.readlines()
    keys = lines[0].strip().split(", ")
    for line in lines[1:]:
        vals = line.strip().split(", ")
    for index in range(len(keys)):
        k = keys[index]
        v = vals[index]
        d1[k] = v
    return d1


def list_word_count(p1: list, result: dict) -> None:
    new_list = []
    for item in p1:
        if item not in new_list:
            new_list.append(item)
    for key in new_list:
        val = p1.count(key)
        result[key] = val



def file_total_words(fname: str, result: dict) -> None:
    with open(fname) as fh:
        lines = fh.readlines()
    words = lines[0].split(" ")
    result["numWords"] = len(words)

'''5. Implment the function file_distinct_words which

takes two input paramters fname, a string representing a file, and result which is a dict
fname has one line, with words separated by spaces
inserts an item in result for each distinct word in fname, the key is the word and the count is the number of times the word occurs in fname
return nothing'''
def file_distinct_words(fname: str, result: dict) -> None:
    with open(fname) as fh:
        lines = fh.readlines()
    words = lines[0].strip().split(" ")
    new_list = []
    for word in words:
        if word not in new_list:
            new_list.append(word)
    for word in new_list:
        key = word
        val = words.count(word)
        result[key] = val
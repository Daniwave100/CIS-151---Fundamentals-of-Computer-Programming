

def convert_str_and_merge(p1: str, p2:str) -> list:
    final_list = []
    final_list2 = []
    list1 = p1.split(",")
    list2 = p2.split(",")
    new_list = list1 + list2
    for val in new_list:
        new_val = val.strip()
        final_list.append(new_val)
    for val in final_list:
        new_val = int(val)
        final_list2.append(new_val)
    return final_list2

def filter_even_numbers(plist: list) -> list:
    new_list = []
    for val in plist:
        if val % 2 == 0:
            new_list.append(val)
    return new_list

def word_counts(plist: list) -> list:
    list1 = []
    for sentence in plist:
        temp_list = sentence.split(" ")
        int_num = len(temp_list)
        list1.append(int_num)
    return list1

def more_consonants_than_vowels(p1: str) -> bool:
    string_list = []
    vowel_num = 0
    consonant_num = 0
    for letter in p1:
        string_list.append(letter)
    for val in string_list:
        if val in "aeiou":
            vowel_num += 1
        else:
            consonant_num += 1
    if consonant_num > vowel_num:
        return True
    else:
        return False

def insert_duplicate(plist: list, p2: int) -> None:
    for index,val in enumerate(plist):
        if val == p2:
            plist.insert(index+1, p2)
            break
'''

takes one input parameter plist, which is a list of ints
modifies plist to remove all even numbers from it
returns nothing

'''

# remove all the even numbers from plist
def remove_all_even_numbers(plist: list) -> None:
    len_plist = len(plist)
    p2 = plist[:]
    for item in p2:
        if item % 2 == 0:
            plist.remove(item)



# string has more than p2 vowels

def num_vowels_gt(p1: str, p2: int) -> bool:
    num_char = 0
    for char in p1:
        if char in "aeiou":
            num_char += 1
    if num_char > p2:
        return True
    else:
        return False

# plist is list of strings, return item with most words
'''takes one input parameter plist, which is a list of strings
each string in plist is one or more words separated by a space
returns the string in plist which has the most words'''
def most_words(plist: list) -> str:
    biggest = 0
    biggest_sentence = ""
    for sentences in plist:
        temp_list = sentences.split(" ")
        if len(temp_list) > biggest:
            biggest = len(temp_list)
            biggest_sentence = sentences
    return biggest_sentence



def vowels_consonants(p1: str) -> str:
    letter_list = []
    my_string = ""
    for letter in p1:
        letter_list.append(letter)

    for letter in reversed(letter_list):
        if letter in "aeiou":
            letter_list.remove(letter)
            letter_list.insert(0, letter)
        else:
            continue

    for letter in letter_list:
        my_string += letter
    return my_string

def university_name_to_email(p1: str) -> str:
    # carnegie melon university -> cmu.edu
    # syracuse university -> syracuse.edu
    # massachussets institute technology -> mit.edu
    # tufts university -> tufts.edu
    abbreviation = ""
    name = p1.split(" ")
    if len(name) >= 3:
        for word in name:
            first_letter = word[0]
            abbreviation += first_letter
        abbreviation += ".edu"
        return abbreviation
    else:
        abbreviation = name[0]
        abbreviation += ".edu"
        return abbreviation
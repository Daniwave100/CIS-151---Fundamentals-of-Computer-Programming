# p1 is a string of 4 words
# return the words in this order: 2, 1, 4, 3
def reorder_words(p1: str) -> str:
    new_list = p1.split(" ")
    my_list = []
    my_list.append(new_list[1])
    my_list.append(new_list[0])
    my_list.append(new_list[3])
    my_list.append(new_list[2])
    my_string = ""
    for word in my_list:
        my_string += word + " "

    my_string = my_string.rstrip()

    return my_string

# p1 is a string of words
# return the first initial from each word in p1 concatenated together
def acronym(p1: str) -> str:
    new_list = p1.split(" ")
    my_list = []
    for word in new_list:
        letter = word[0:1]
        letter = letter.upper()
        my_list.append(letter)

    my_string = ""
    for letter in my_list:
        my_string += letter

    return my_string

# p1 is a string
# return the first 3 chars of p1, capitalized
def first_three_chars(p1: str) -> str:
    my_string = p1[0:3]
    new_string = ""
    for letter in my_string:
        letter = letter.upper()
        new_string += letter
    return new_string

# p1 has two or three words
# if p1 has 2 words, return the first 3 chars of the first word
# if p1 has 3 words, return the first 3 letters of each word concatenated together

def two_cases(p1: str) -> str:
    my_list = p1.split(" ")
    my_string = ""
    my_list2 = []
    if len(my_list) == 2:
        value = my_list[0]
        value = value[0:3]
        for letter in value:
            letter = letter.upper()
            my_string += letter
    else:
        for word in my_list:
            letter = word[0:1]
            letter = letter.upper()
            my_string += letter
    return my_string


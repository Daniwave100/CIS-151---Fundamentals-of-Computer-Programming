'''

5. Implement the function next_vowel which

takes one input param p1, a lowercase, one character string from a-z
returns the next vowel in the alphabet
In other words:
    if p1 is a, returns a
    if p1 is b, c, d or e, returns e
    if p1 is e, f, g, h or i, returns i
    if p1 is j, k, l, m, n or o, returns o
    if p1 is p, q, r, s, t, or u, returns u
    if p1 is v, w, x, y, or z, returns a
hint: try using the included function next_char in a while loop

'''
def get_list_of_words(string_param: str) -> list:
    new_list = string_param.split(" ")
    return new_list

def make_sentence(list_param: list) -> str:
    my_string = ""
    for word in list_param:
        my_string += word + " "
    my_string = my_string[:-1]
    return my_string

def reverse_words(string_param: str) -> str:
    my_string = ""
    my_list = string_param.split(" ")
    my_list.reverse()
    for word in my_list:
        my_string += word + " "
    my_string = my_string[:-1]
    return my_string

def floor_log_base_2(p1: int) -> int: # while loop?
    times = 0
    while (p1 // 2) != 0:
        p1 = p1 // 2
        times += 1
    return times

def next_char(p1: str) -> str: # if it gives you an a, give b, if z, a and so on
    if len(p1) != 1 or not p1.islower():
        return p1

    val = ord(p1) + 1
    if val > ord("z"):
        val -= 26
    return chr(val)

def next_vowel(p1:str) -> str: # while loop
    while p1 not in "aeiou":
        p1 = next_char(p1)
    return p1

    # if ord(p1) == ord("a"):
    #     return "a"
    # elif ord(p1) <= ord("e"):
    #     return "e"
    # elif ord(p1) <= ord("i"):
    #     return "i"
    # elif ord(p1) <= ord("o"):
    #     return "o"
    # elif ord(p1) <= ord("u"):
    #     return "u"
    # else:
    #     return "a"

# 4 problems
# 2 string manipulation
# 1 simple accumulation loop
# 1 slightly complicated accumulation loop
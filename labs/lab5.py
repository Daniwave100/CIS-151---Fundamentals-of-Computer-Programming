def right_justify(p1: str) -> str:
    if len(p1) > 3:
        return "---"
    if len(p1) == 3:
        return p1
    if len(p1) == 2:
        return " " + p1
    if len(p1) == 1:
        return "  " + p1
    if p1 == "":
        return "   "

def sum_up_to(p1: int) -> int:
    result = 0
    for num in range(p1):
        result = result + num
    return result

def sum_beg_end(p1: int, p2: int) -> int:
    result = 0
    if p1 > p2:
        return 0
    if p1 <= p2:
        for num in range(p1, p2):
            result += num
        return result


def is_vowel(p1: str) -> str:
    if len(p1) > 1:
        return False
    if (p1 != "a" or p1 != "e" or p1 != "i" or p1 != "o" or p1 != "u"):
        if len(p1) > 1:
            return False
        elif (len(p1) == 1) and (p1 == "a" or p1 == "e" or p1 == "i" or p1 == "o" or p1 == "u"):
            return True
    else:
        return False


def prepend_if_even(p1: int, p2: str) -> str:
    if p1 % 2 == 1:
        return p2
    else:
        return "even" + p2

def fizzbuzz(p1: int) -> str:
    if (p1 % 3 == 0) and (p1 % 5 == 0):
        return "fizzbuzz"
    if p1 % 3 == 0:
        return "fizz"
    if p1 % 5 == 0:
        return "buzz"
    else:
        return ""
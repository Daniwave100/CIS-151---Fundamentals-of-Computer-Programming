

def test_if_true(p1: bool) -> bool:
    result = False
    if p1 == True:
        result = True
    return result


def test_if_empty(p1: str) -> bool:
    result = False
    if len(p1) == 0:
        result = True
    return result


def return_smaller_int(p1: int, p2: int) -> int:
    result = p2
    if p1 < p2:
        result = p1
    return result


def return_shorter_param(p1: str, p2: str) -> str:
    result = p2
    if len(p1) < len(p2):
        result = p1
    return result


def either_or_true(p1: bool, p2: bool) -> bool:
    result = False
    if (p1 == True) or (p2 == True):
        if not((p1 == True)  and (p2 == True)):
            result = True
    return result


def either_or_even(p1: int, p2: int) -> bool:
    result = False
    if ((p1 % 2) == 0) or ((p2 % 2) == 0):
        if not((p1 % 2 == 0) and (p2 % 2 == 0)):
            return True
    return result

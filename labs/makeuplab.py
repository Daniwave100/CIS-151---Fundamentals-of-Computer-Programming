

# *** I should mention, I did this lab from home for extra practice ***

'''1. Implement the function abbreviate which

takes one input parameter p1 which is a string
p1 is either one, two or three words, separated by spaces
if p1 is one word, returns the first three chars of the first word
if p1 is 2 words, returns the first two chars of the first word concatenated with the first char of the second word
if p1 is 3 words, returns the first char of each word'''
def abbreviate(p1: str) -> str:
    print(p1)
    p1List = p1.split(" ")
    if len(p1List) == 1:
        return p1[:3]
    elif len(p1List) == 2:
        firstTwoChar = p1List[0][:2]
        secondOneChar = p1List[1][:1]
        myString = firstTwoChar + secondOneChar
        return myString
    else:
        firstChar = p1List[0][:1]
        secondChar = p1List[1][:1]
        thirdChar = p1List[2][:1]
        myString = firstChar + secondChar + thirdChar
        return myString

'''2. Implement the function convert_address_list which

takes one input parameter p1 which is a list of ints and strings
returns a list which is copy of p1 except that all items are strings
does not change p1'''
def convert_address_list(p1: list) -> list:
    myString = "hello"
    myNum = 1
    newList = []
    for item in p1:
        if type(item) == type(myString):
            newList.append(item)
        else:
            item = str(item)
            newList.append(item)
    return newList

'''3. Implement the function two_largest_ints which

takes one input parameter p1, which is a list of ints
returns a list of the two largest ints in p1, larger first
does not change p1'''
def two_largest_ints(p1: list) -> list:
    p1Copy = p1[:]
    myList = []
    bigNum = max(p1Copy)
    myList.append(bigNum)
    p1Copy.remove(bigNum)


    bigNum2 = max(p1Copy)
    myList.append(bigNum2)
    return myList




'''4. Implement the function num_failing_lab_scores which

takes one input parameter p1 which is a dict
looks at all items in p1 which have a key which starts with "lab"
counts and returns how many such items have scores less than 50'''
def num_failing_lab_scores(p1: dict) -> int:
    numLessFifty = 0
    for key,val in p1.items():
        if key[:3] == "lab":
            val = int(val)
            if val < 50:
                numLessFifty += 1

    return numLessFifty

'''5. Implement the function last_half_backwards which

takes one input parameter p1 which is a string
return the second half of p1, reversed'''
def last_half_backwards(p1: str) -> str:
    lenHalf = len(p1) // 2
    secondHalf = p1[lenHalf:]
    secondHalf = secondHalf[::-1]
    print(secondHalf)
    return secondHalf

# *** I should mention, I did this lab from home for extra practice ***
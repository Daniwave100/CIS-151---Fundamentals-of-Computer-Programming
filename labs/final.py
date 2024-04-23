'''1. Implement the function convert_to_yaml which
takes one input parameter, p1 which is a string
p1 will always have a lab number, then a space, and then a score
return a string which puts "scores\n\t" before the lab number, then a ": ",
then the score, and finally a "\n"'''

# input: p1 = "lab1 88"
# return "scores\n\tlab1: 88\n"
def convert_to_yaml(p1: str) -> str:
    stringList = p1.split(" ")
    val = f"scores\n\t{stringList[0]}: {stringList[1]}\n"
    return val
    pass


'''2. Implement the function total_len_of_strs which
takes one input parameter p1, which is a list of strings and ints
return the total length of all the strings in p1'''
# accumulate int result over list
# input is a list of strings and ints
# return len of all the strings in list
def total_len_of_strs(p1: list) -> int:
    result = 0
    for val in p1:
        if type(val) == type("hello"):
            result += len(val)
    return result

'''3. Implement the function list_of_even_ints which
takes one input parameter p1, which is a list of strings
some strings in p1 are just digits, the rest have no digits
return a list of the even numbers from p1'''
def list_of_even_ints(p1: list) -> list:
    newList = []
    finalList = []
    for val in p1:
        try:
            val = int(val)
            newList.append(val)
        except:
            print("Error occured")
    print(newList)
    for val in newList:
        if val % 2 == 0:
            val = str(val)
            finalList.append(val)

    return finalList

'''4. Implement the function just_exam_scores which
takes one input parameter p1, which is a dictionary
p1 has one item with key "midterm", another item with key "final" and many items with key "lab*" where * is a number from 1 to 24
all values in p1 are ints, or lists of ints, representing scores
return a dictionary with two items one for the midterm score, and the other for the final score'''
# input = {lab1: 88, lab2: 82, midterm:99, final: 91, lab3: 88}
# input = {lab1: 88, lab2: 82, midterm:[99, 88], final: 91, lab3: 88}
# scores may be lists; return max of list
def just_exam_scores(p1: dict) -> dict:
    d1 = {}
    midtermScore = p1["midterm"]
    finalScore = p1["final"]
    if type(midtermScore) == type([]):
        midtermScore = max(midtermScore)
    if type(finalScore) == type([]):
        finalScore = max(finalScore)
    d1["midterm"] = midtermScore
    d1["final"] = finalScore
    return d1

'''5. Implement the function biggest_class which
takes one input parameter p1, which is a list of lists
each item in p1 is a two item list, int suid and str class
return a str for the class which has the most students'''
# courses = [[1, "cis151"], [0, "cis151"],
#            [2, "ecs101"], [0, "ecs101"], [3, "ecs101"],
#            [0, "mat193"],
#            [1, "mat295"],
#            [2, "mat296"],
#            [1, "che106"],
#            [2, "fys101"]]
# return "ecs101"
def biggest_class(courses: list) -> str:
    d1 = {}
    myNum = 0
    for list in courses:
        d1[list[1]] = list[0]
    print(d1)
    for key,val in d1.items():
        if val == 3:
            myString = key
            myNum += 1
    return myString



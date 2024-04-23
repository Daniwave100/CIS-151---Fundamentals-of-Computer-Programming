'''1. Implement the function package_dicts which

takes two input params d1 and d2 both dictionaries
returns a list whose first item is d1 and second is d2'''
def package_dicts(d1: dict, d2: dict) -> list:
    my_list = []
    my_list.append(d1)
    my_list.append(d2)
    return my_list

'''2. Implement the function cumulative_grade which

takes one input parameter d1, which is a dictionary
d1 is guaranteed to have keys "name", "midterm" and "final"
d1 may have one or many keys for labs
each key for a lab will have the word lab follwed by a number
computes a cumulative score = 0.6 (average of lab scores) + 0.2 midterm score + 0.2 final score
returns a dictionary with a key "name" and value of name from d1
and a key "cumulative_score" and value the computed cumulative score'''
def cumulative_grade(d1: dict) -> dict:
    name = ""
    lab_total = 0
    num_lab = 0
    midterm = 0
    final = 0
    d2 = {}

    for key, val in d1.items():
        if key == "name":
            name = val
        elif key[:3] == "lab":
            lab_total += val
            num_lab += 1
        elif key == "midterm":
            midterm += val
        elif key == "final":
            final += val
        else:
            continue

    lab_score = lab_total / num_lab
    final_grade = (lab_score * 0.6) + (midterm * 0.2) + (final * 0.2)

    d2["name"] = name
    d2["cumulative_score"] = final_grade

    return d2

'''3. Implement the function gradebook which

takes two input parameters key_names, which is a list of strings and fname which is a string
each line in fname has a name, a space and a set of scores separated by colon
forms a dictionary from keys_names and the contents of each line
returns a list of dictionaries, one dictionary for each line

{'name': 'joe', 'lab1': '87', 'lab2': '46', 'midterm': '91'}
'''
def gradebook(key_names: list, fname: str) -> list:
    jen = {}
    joe = {}
    l1 = []
    final_list = []
    with open(fname) as fh:
        lines = fh.readlines()




    for line in lines:
        line = line.replace(" ", ":")
        line = line.strip()
        l1.append(line)

    jen = l1[0]
    joe = l1[1]

    key_names = ["name", "lab1", "lab2", "midterm"]


    jen_list = jen.split(":")
    jen = dict(zip(key_names, jen_list))


    joe_list = joe.split(":")
    joe = dict(zip(key_names, joe_list))

    final_list.append(jen)
    final_list.append(joe)


    return final_list







'''4. Implement the function dict_from_file which

takes one input parameter fname, which is a string
each line in fname has a name, a space and a set of scores separated by colon
returns a dictionary whose keys are all the names and values are lists of scores'''
def dict_from_file3(fname: str) -> dict:
    my_list = []
    d1 = {}

    with open(fname) as fh:
        lines = fh.readlines()

    for line in lines:
        temp_list = line.strip().split()
        my_list.append(temp_list)

    set1 = my_list[0]
    set2 = my_list[1]
    set3 = my_list[2]

    num1 = set1[1].split(":")
    num2 = set2[1].split(":")
    num3 = set3[1].split(":")

    d1[set1[0]] = num1
    d1[set2[0]] = num2
    d1[set3[0]] = num3

    return d1


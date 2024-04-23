'''1. Implement the function convert_list which

takes one input parameter scores, which is a list of ints
modifies scores so that each item is a list with the original item'''
def convert_list(scores: list) -> None:
    for index in range(len(scores)):
        scores[index] = [scores[index]]
    pass

'''2. Implment the function avg_score which

takes one input parameter scores, which is a dictionary
computes and returns the average score of all the int values in scores
(hint: integer division)'''
def avg_score(score: dict) -> int:
    avg_score = 0
    total_sum = 0
    for key, val in score.items():
        total_sum += val

    avg_score = total_sum // len(score)

    return avg_score

'''3. Implement the function dict_from_file2 which

takes one input parameter fname, which is a string and represents a filename
reads the file pointed to by fname, which may have more than one line
returns a dictionary of string keys and list-of-int values'''
def dict_from_file2(fname: str) -> dict:
    d1 = {}
    my_list = []
    with open(fname) as fh:
        lines = fh.readlines()

    for line in lines:
        temp_list = line.strip().split(", ")
        my_list += temp_list
    print(my_list)

    for item in my_list:
        key, val = item.split(" ")
        key = key.strip("(")
        d1[key] = []

    for item in my_list:
        key, val = item.split(" ")
        key = key.strip("(")
        val = val.strip(")")
        val = int(val)
        d1[key].append(val)

    return d1

'''4. Implement the function read_two_files which

takes two input parameters fname1 and fname2, both of which are string, representing filenames
reads both file, which may have more than one line
returns a dictionary of string keys and list-of-int-values
(hint: dict_from_file2)

'''
def read_two_files(fname1: str, fname2: str) -> dict:
    my_list1 = []
    my_list2 = []
    my_list3 = []
    d1 = {}
    with open(fname1) as fh1:
        lines1 = fh1.readlines()
    with open(fname2) as fh2:
        lines2 = fh2.readlines()
    for line in lines1:
        temp_list = line.strip().split(", ")
        my_list1 += temp_list
    for line in lines2:
        temp_list = line.strip().split(", ")
        my_list2 += temp_list

    my_list3 = my_list1 + my_list2

    for item in my_list3:
        key, val = item.split(" ")
        key = key.strip("(")
        d1[key] = []

    for item in my_list3:
        key, val = item.split(" ")
        key = key.strip("(")
        val = val.strip(")")
        val = int(val)
        d1[key].append(val)

    return d1

'''5. Implement the function write_dict_to_file which

takes two input params scores, which is dictionary and fname, which is a string
writes a line into fname for each item in scores
(hint: str method join() can convert a list of strings to a string)'''
def write_dict_to_file(scores: dict, fname: str) -> None:
    with open(fname, "w") as fh:
        for key, val in scores.items():
            print(val)
            # for v in val:
                # val = str(val)
            val = ", ".join(val)
            fh.write(f"{key}: {val}\n")
    pass
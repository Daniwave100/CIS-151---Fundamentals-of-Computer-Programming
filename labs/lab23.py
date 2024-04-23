'''For both questions, the data file has the same format.

The first line is a header, column names separated by comma space.
All following lines are data lines, values separated by comma space.
For example:

name, lab1, lab2, midterm, lab3, final
joe, 88, 81, 90, 84, 91
jen, 87, 85, 92, 80, 93
...'''
# read file
# first line is header:
# name, lab1, lab2, lab3, midterm, lab4, lab5, final
# rest of lines are data:
# jen, 88, 81, 82, 90, 80, 84, 90
# joe, 88, 81, 82, 90, 80, 84, 90
# return list of dicts

'''1. Implement the function gradebook1 which

reads the data file and returns a list of dictionaries
each dictionary has the column names as keys, and the data from one line as values'''
def gradebook1(fname: str) -> list:
    d1_list = []
    with open(fname) as fh:
        lines = fh.readlines()

    temp_keys = lines[0]
    keys = temp_keys.strip().split(", ")
    print(keys)

    temp_vals = lines[1:]
    for val in temp_vals:
        val_list = val.strip().split(", ")
        d1 = dict(zip(keys, val_list))
        d1_list.append(d1)
    return d1_list


# return dict of lists
# {"name": ["jen", "joe"], lab1:[]...}
'''2. Implement the function gradebook2 which

reads the data file and returns a dictionary
each key in the dictionary is one of the column names
each value in the dictionary is a list of all the data for one of the columns'''
def gradebook2(fname: str) -> dict:
    result = {}
    with open(fname) as fh:
        lines = fh.readlines()

    temp_keys = lines[0]
    keys = temp_keys.strip().split(", ")
    for index in range(len(keys)):
        result[keys[index]] = []
    print(result)

    temp_vals = lines[1:]
    for val in temp_vals:
        val_list = val.strip().split(", ")
        for index in range(len(val_list)):
            # keys[index].append(val_list[index])
            key = keys[index]
            result[key].append(val_list[index])

    return result


        # iterate over val_list, use in index loop

    # {"name":["joe", "jen", "..."], "lab1":[]

# result.key.append(val)

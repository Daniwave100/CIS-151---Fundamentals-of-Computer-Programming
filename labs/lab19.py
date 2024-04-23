'''1. Implement the function string_to_dict which

takes one input parameter p1, which is a str
p1 is a series of names and scores.
returns a dictionary of name:score pairs, both name and score are str'''

def string_to_dict(p1: str) -> dict:
    d1 = {}
    keys, vals = p1.split("|")
    key_list = keys.split(", ")
    val_list = vals.split(", ")
    for index in range(len(key_list)):
        key = key_list[index]
        val = val_list[index]
        key = key.strip()
        val = val.strip()
        d1[key] = val
    return d1

'''2. Implement the function write_list_to_file which

takes two input parameters, plist which is a list of strings, and fname which is a string
opens a file to fname, and writes each item from plist to a line in fname
returns nothing'''
def write_list_to_file(plist: list, fname: str) -> None:
    with open(fname, "w") as fh:
        for item in plist:
            fh.write(f"{item}\n")

'''3. Implement the function max_and_min which

takes one input parameter fname, which is a str
opens and reads all the lines from fname
each line in fname is a name and score separated by colon space
returns a dictionary with an item the max and min scores from fname'''

def max_and_min(fname: str) -> dict:
    d1 = {}
    d2 = {}
    values = []
    with open(fname) as fh:
        lines = fh.readlines()
    for line in lines:
        key, val = line.strip().split(": ")
        values.append(int(val))
    maximum = max(values)
    minimum = min(values)

    d2["max"] = maximum
    d2["min"] = minimum
    return d2

    print(d1)

    return d2

# think about word counts, hardest
'''4. Implement the function names_to_scores which

takes one input parameter fname, which is a str
opens and reads all the lines from fname
each line in fname is a name and score separated by colon space
returns a dictionary with an item for each name, and the value is the scores for that name in a list'''
def names_to_scores(fname: str) -> dict:
    d1 = {}
    l1 = []
    l2 = []
    with open(fname) as fh:
        lines = fh.readlines()
    for line in lines:
        keys, vals = line.strip().split(": ")
        d1[keys] = []

    for line in lines:
        keys, vals = line.strip().split(": ")
        d1[keys].append(vals)
    return d1

'''5. Implement the function scores_to_names which

takes one input parameter fname, which is a str
opens and reads all the lines from fname
each line in fname is a name and score separated by colon space
returns a dictionary with an item for each score, and the value is the names for that score in a list'''
def scores_to_names(fname:str) -> dict:
    d1 = {}
    with open(fname) as fh:
        lines = fh.readlines()
    for line in lines:
        vals, keys = line.strip().split(": ")
        d1[keys] = []

    for line in lines:
        vals, keys = line.strip().split(": ")
        d1[keys].append(vals)
    return d1
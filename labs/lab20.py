'''1. Implement the function populate_dict which

takes two input parameters keyNames which is a list, and fname which is a str
fname will have one line with a name and scores separated by comma space
returns a dictionary with keys from keyNames and corresponding values from the file'''
def populate_dict(keyNames: list, fname: str) -> dict:
    d1 = {}
    with open(fname) as fh:
        lines = fh.readlines()
    for line in lines:
        scores_list = line.strip().split(", ")

    for index in range(len(scores_list)):
        key = keyNames[index]
        val = scores_list[index]
        d1[key] = val
    return d1

'''2. Implement the function dict_from_file which

takes one input parameter fname which is a str
opens and reads the file pointed to by fname which will contain one line
creates an item in a dict for each (name val) pair read from fname
returns the dictionary created'''
def dict_from_file(fname: str) -> dict:
    d1 = {}
    with open(fname) as fh:
        lines = fh.readlines()
    for line in lines:
        my_list = line.strip().split(", ")
    print(my_list)
    for item in my_list:
        item = item.replace("(", "")
        item = item.replace(")", "")
        key, val = item.split(" ")
        val = int(val)
        d1[key] = val
    return d1
    pass

'''3. Implement the function write_dict_to_file which

takes two parameters score, which is a dict, and fname which is a string
writes each item from score to a line in fname
returns nothing'''
def write_dict_to_file(score: dict, fname: str) -> None:
    with open(fname, "w") as fh:
        for key, val in score.items():
            fh.write(str.format("{0}: {1}\n", key, val))
            # fh.write(key)
            # fh.write(":")
            # val = str(val)
            # fh.write(" ")
            # fh.write(val)
            # fh.write("\n")

'''4. Implement the function num_failing_scores which

takes one input parameter gradebook, which is a dict
each item in gradebook is a name key and a score values
returns an int matching the number of scores in gradebook that are under 50'''
def num_failing_scores(gradebook: dict) -> int:
    x = 0
    for key, val in gradebook.items():
        if val < 50:
            x += 1
    return x

    pass


# return len([x for x in d1.values() if x < 50])
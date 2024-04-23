'''

4. Implement a function last_half_backwards which:

takes one input parameter plist, a list of ints
returns a list with all the items from the last half of plist, in reverse order
if plist has an odd number of items, consider the middle item part of the back half
removes all the items from the last half of plist

'''

def sum_range(plist: list, beg: int, end: int) -> int:
    if len(plist) == 0:
        return 0
    elif beg == end:
        return 0
    elif beg > end:
        return 0
    else:
        mylist = plist[beg:end]
        sum_mylist = sum(mylist)
        return sum_mylist

def every_other_item(plist: int) -> list:
    mylist = plist[0::2]
    return mylist

def last_half(plist: list) -> list:
    mylist = []
    half_plist = len(plist) // 2
    if len(plist) % 2 == 0:
        my_list = plist[half_plist::]
    else:
        my_list = plist[half_plist::]
    return my_list

def last_half_backwards(plist: list) -> list:

    my_list = last_half(plist)
    finish_list = my_list[::-1]

    for num in finish_list:
        plist.remove(num)

    return finish_list

def selection_sort(plist: list) -> list:
    result = []
    for x in range(len(plist)):
        minimum = min(plist)
        result.append(minimum)
        plist.remove(minimum)
    return result
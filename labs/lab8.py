'''

5. Implement a function get_domain_from_url which
  takes one input parameter p1, of type str
  p1 will be a url of 4 possible forms, see test for details
  returns the domain for a url which matches any one of the 4 possible forms
  returns "" for any input that doesn't match the 4 possible forms

'''

def magic_index(p1: list) -> int:
    for index, value in enumerate(p1):
        if index == value:
            return value
    return -1

def longer_than(plist: list, p2: str) -> str:
    for item in plist:
        if len(item) > len(p2):
            return item
    return ""

def num_longer_than(plist: list, p2: str) -> int:
    count = 0
    for item in plist:
        if len(item) > len(p2):
            count += 1
    return count

def get_second_index(p1: str, p2: str) -> int:
  if p1.count(p2) > 1:
    first_index = p1.find(p2)
    second_index = p1.find(p2, first_index+1)
    return second_index
  return -1

def get_third_index(p1: str, p2: str) -> int:
    if p1.count(p2) > 2:
        first_index = p1.find(p2)
        second_index = p1.find(p2, first_index + 1)
        third_index = p1.find(p2, second_index + 1)
        return third_index
    else:
        return -1

def get_domain_from_url(p1: str) -> str:
    if p1.startswith("http"):
        url_split = p1.split("/")
        website = url_split[2]
        return website
    elif p1.startswith("ftp"):
        url_split = p1.split("@")
        url_second = url_split[1]
        slash_split = url_second.split("/")
        website = slash_split[0]
        return website
    elif p1.startswith("mailto"):
        url_split = p1.split("@")
        url_second = url_split[1]
        slash_split = url_second.split("/")
        website = slash_split[0]
        return website
    else:
        return ""

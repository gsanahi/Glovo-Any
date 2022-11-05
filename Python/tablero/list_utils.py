from itertools import count


def find_one(list,needle):
    found = False
    i = 0

    while not found and i < len(list):
        if list[i] == needle:
            found = True
        else:
            found = False
        i = i + 1
    return found

def find_n(list,needle,n):
    i = 0
    count = 0

    while (count < n) and (i < len(list)):
        if needle == list[i]:
            count += 1
        

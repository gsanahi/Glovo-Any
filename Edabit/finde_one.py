def find_one(list,needle):
    found = False

    for element in list:
        if needle == element:
            found = True 
            break
    return found

print (find_one([1,4,5,6,7,7], 6))


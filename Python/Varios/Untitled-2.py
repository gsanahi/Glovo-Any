def find_one(list, needle):
    found = False
    index = 0

    while not found and index < len(list):
        if needle == list[index]:
            found = True
        else:
            found = False
        index = index + 1 

    return found

    def find_n(list, needle, n):
    
        index = 0
        count = 0
  
    while count < n and index < len(list):
         
        if needle == list[index] :
            count = count + 1

        index = index + 1
    
    return count >= n
def is_sorted(arr): #arr -> Bool
    for i in range(0,len(arr)):
        if i < len(arr)-1:
            if arr[i] > arr[i+1]:
                return False
    
    return True


print(is_sorted([2,3,4]))
print(is_sorted([5,3,4]))
print(is_sorted([1,1,1]))
print(is_sorted([2,3,4,1]))

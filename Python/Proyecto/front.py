def validity(matrix):
    return type_of(matrix) and is_equal(matrix) and is_num(matrix)
            
       
def type_of(matrix):  
    if not isinstance(matrix,list):
            return False
    for i in range(0,len(matrix)):
        if not isinstance(matrix[i],list):
            return False
    return True  

def is_equal(matrix):
    for i in range(0, len(matrix)-1):
        if len(matrix[i]) != len(matrix[i+1]):
            return False
    return True

def is_num(matrix):
    for i in range (0,len(matrix)):
        for j in range(0, len(matrix[i])):
            if not isinstance(matrix[i][j],int):
                return False
        
    return True



matrix = [[0,2,1,3,4,1],    #0
          [1,2,3,4,5,3],    #1
          [2,2,3,1,0,5],    #2
          [1,0,5,1,2,1],    #3
          [1,7,2,0,3,9]]    #4
        #  0 1 2 3 4 5 

m = [[], (0,5)] 

x = [[0,2,1,3,4,1],    #0
     [1,'a',3,4,5,3],    #1
     [2]]
# print(in_numeral_matrix(matrix))

print("Test")
print(validity(m))

print("Fin test")
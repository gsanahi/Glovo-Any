from matrix import process_matrix

def in_numeral_matrix(matrix):   #List[list] -> Bool
    validity = True
    for i in range (0,len(matrix)):
        if matrix[i]:               #Si no esta vacia, o sea si me da True
            if len(matrix[i]) == len(matrix[i+1]):   #Compruebo que el tamaño de las listas sean iguales
                    validity = True
            for j in range(len(matrix[i])):         #Compruebo que todos los elementos sean del tipo Int
                if isinstance(matrix[i][j], int):
                    validity = True
                
        else:
            validity = False
    return validity



matrix = [[0,2,1,3,4,1],    #0
          [1,2,3,4,5,3],    #1
          [2,2,3,1,0,5],    #2
          [1,0,5,1,2,1],    #3
          [1,7,2,0,3,9]]    #4
        #  0 1 2 3 4 5 

m = [[],[],[],[],[]] 

# print(in_numeral_matrix(matrix))

print("Test")
arr = []
for i in range(0, len(arr)):
    print("Paso")

print("Fin test")
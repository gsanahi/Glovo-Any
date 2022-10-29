def process_matrix(matrix):
    '''
    Recibo una lista de lista de ints y devuelvo una nueva lista de listas de ints
    modificados (con el promedio de los vecinos segun corresponda)
    '''
    # creo la nueva matrix
    new_matrix = []
    
    # recorro todos los elementos de mi matrix
    for i in range(0,len(matrix)): # recorro por filas
        new_list = []  
        for j in range(0, len(matrix[i])):   # recorro por columnas
            value = sum_neighbours(i,j,matrix)  
            new_list.append(value)
            
        new_matrix.append(new_list)

    # muestro mi nueva matriz creada
    return new_matrix


def sum_neighbours(i,j,matrix): # num,num, Matrix -> num
    '''
    funcion para saber el valor de mis vecinos y sumarlos con el mio en caso que sea posible
    '''
    my_value = matrix[i][j]                    # donde estoy parado, el element
    neighbours = 1                             # me cuento a mi mismo primero

    if j < len(matrix[i])-1:                    # voy a la derecha
        my_value += matrix[i][j+1]              # sumo el valor
        neighbours +=1                          # sumo uno a cantidad de vecinos
        
    if j > 0:                                   # voy para la izquierda
        my_value += matrix[i][j-1]
        neighbours +=1

    if i > 0:                                   # voy para arriba
        my_value += matrix[i-1][j]
        neighbours +=1

    if i < len(matrix)-1:                      # voy para abajo
        my_value += matrix[i+1][j]
        neighbours +=1

    return round(my_value / neighbours,2)

    


#Tests:
matrix = [[0,2,1,3,4,1],    #0
          [1,2,3,4,5,3],    #1
          [2,2,3,1,0,5],    #2
          [1,0,5,1,2,1],    #3
          [1,7,2,0,3,9]]    #4
        #  0 1 2 3 4 5 

m = [[],[],[],[],[]] 

#print(process_matrix(matrix))
#print(process_matrix(m))


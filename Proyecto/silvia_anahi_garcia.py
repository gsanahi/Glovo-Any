def process_matrix(matrix):
    '''
    Funcion para validar que los datos de la matriz sean los correctos. 
    Esto es responsabilidad del frontend. 
    '''
    validity(matrix)
    __process_matrix(matrix)   # Entro a la funcion propia del backend


def __process_matrix(matrix):
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

####### Funciones para validar #######

def validity(matrix):
    if not is_matrix(matrix):
        raise ValueError('Only works on matrices')

    if not is_row_same_length(matrix):
        raise ValueError('Only works on rows with same length')
    
    if not is_num(matrix):
        raise ValueError('Only works on numerical matrices')

def is_matrix(matrix):  
    if not isinstance(matrix,list):
            return False
    for i in range(0,len(matrix)):
        if not isinstance(matrix[i],list):
            return False
    return True  

def is_row_same_length(matrix):
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


####Tests####
test_valid_matrix = [[0,2,1,3,4,1],
                     [1,2,3,4,5,3],
                     [2,2,3,1,0,5],
                     [1,0,5,1,2,1],
                     [1,7,2,0,3,9]]    

test_valid_empty = [[],[],[],[],[]] 

test_invalid_different_len = [[0,2,1,3,4,1],    
                            [1,3,4,5,3],    
                            [2]]

test_invalid_type = [[0,2,1,3,4,1],['a']]




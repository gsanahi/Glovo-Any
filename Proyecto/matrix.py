from Proyecto.process_list import process_list


def process_matrix(matrix):
    '''
    Recibo una lista de lista de ints y devuelvo una nueva lista de listas de ints
    modificados (con el promedio de los vecinos segun corresponda)
    '''
    # creo la nueva matrix
    new_matrix = []
    # recorro todos los elementos de mi matrix
    for i in range(0,len(matrix)):   # recorro por filas
        for j in range(0, len(matrix[i])):   # recorro por columnas
            element = matrix[i][j]
#            new_matrix.append(new_value_list)
    # muestro mi nueva matriz creada
    return new_matrix

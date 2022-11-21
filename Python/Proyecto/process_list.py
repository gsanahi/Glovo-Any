from functools import reduce

def process_list(elements):
    '''
    Recibe una lista de numeros y devuelve una nueva con los elementos cambiados.
    Cada elemento dela nueva sera el promedio del valor antiguo y el de sus vecinos
    '''
    #Creo una lista vacia donde ire acumulando
    processed_list =[]
    if len(elements) == 1:
        processed_list = elements
    else:
        # Por cada elemento de la lista...
        for index, element in enumerate(elements):
            #Lo proceso
            new_element = process_element(index,element)
            # lo añado a la lista
            processed_list.append(new_element)

    #devuelvo la nueva lista
    return processed_list

def process_element(index,elements):
    '''
    Recibe el indice de un elelemtno y la lista en la que esta, calcula su promedio con sus vecinos
    y devuelve dicho promedio
    '''
    # Obtengo la lista de vecinos
    indices = get_neighbours_indices(index, elements)
    values = get_neighbour_values(indices,elements)
    # Calculo su promedio
    average = get_average(values)

    # Devuelvo el valor final
    return average   

def get_neighbours_indices(index, elements):
    '''
    Devuelve la lista de indices de vecinos incluyendo el propio
    '''
    indices = []
    if index == 0:
        # el primero
        indices.append(index + 1) 
    elif index == len(elements)-1:
        #el ultimo
        indices.append(index - 1) 
    else:
        indices.append(index + 1)
        indices.append(index - 1)
    # incluyo al propio elemento como vecino de si mismo
    indices.append(index)

def get_neighbour_values(indices, elements):
    values = []
    for index in indices:
        values.append(elements[index])
    return values


def get_average(values):
    '''
    Recibe una lista de numeros y devuelve su promedio
    '''
    return reduce(lambda x,y : x + y,values,0)/ len(values)

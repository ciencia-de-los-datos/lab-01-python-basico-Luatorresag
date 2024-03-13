"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
        data_1 = []
        for line in data:
            line = line.split("\t")
            data_1.append(line[1])
        data_1 = [int(i) for i in data_1]
        suma = 0
        for n  in data_1:
            suma = suma + n 
       
    return suma

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    first_letters = []
    count_letter = {}
    for line in data:
        line = line.split("\t")
        first_letters.append(line[0])
    first_letters.sort()
    for letter in first_letters:
        if letter in count_letter:
            count_letter[letter] += 1
        else:
            count_letter[letter] = 1
    resultado = []
    for tuple_ in count_letter:
        resultado.append((tuple_,count_letter[tuple_]))
        
    return resultado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    data_1 = [(line.split("\t")[0], int(line.split("\t")[1])) for line in data]
    data_1 = sorted(data_1)
    sum_letter = {}
    for element in data_1:
        if element[0] in sum_letter:
            sum_letter[element[0]] += element[1] 
        else:
            sum_letter[element[0]] = element[1]
            
    result = [(key, sum_letter[key]) for key in sum_letter]        
    # result = [(key, value) for key, value in sum_letter.items()]        
    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    data_1 = [line.split("\t")[2] for line in data]
    data_1 = [line.split("-")[1] for line in data_1]
    # data_1 =  sorted(data_1)
    count_month = {}
    
    for element in data_1:
        if element in count_month:
            count_month[element] += 1
        else:
            count_month[element] = 1

    result = [(key, count_month[key]) for key in count_month]       
    result = sorted(result)
    
    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    data_1 = [(line.split("\t")[0], int(line.split("\t")[1])) for line in data]
    max_min = {}
    for elem in data_1:
        if elem[0] in max_min:
            max = max_min[elem[0]][0]
            min = max_min[elem[0]][1]
            if max < elem[1]:
                max = elem[1]
            if min > elem[1]:
                min = elem[1]

            max_min[elem[0]] = [max, min]
        
        else:
            max_min[elem[0]] = [elem[1], elem[1]]
    
    result = [(key,value[0], value[1]) for key, value in max_min.items() ]
    result = sorted(result)
 
    
    return result

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()       
    data_1 = [line.split("\t")[4].strip() for line in data]
    data_1 = [elemt.split(",") for elemt in data_1]
    data_1 = [(elemt.split(":")[0], int(elemt.split(":")[1])) for lista in data_1 for elemt in lista]
    min_max = {}
    for elem in data_1:
        if elem[0] in min_max:
            min = min_max[elem[0]][0]
            max = min_max[elem[0]][1]
            if max < elem[1]:
                max = elem[1]
            if min > elem[1]:
                min = elem[1]

            min_max[elem[0]] = [min, max]
        else:
            min_max[elem[0]] = [elem[1], elem[1]]
    
    result = [(key,value[0], value[1]) for key, value in min_max.items()] 
    result = sorted(result)
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 1 y una lista con todas las letras asociadas (columna 0)
    a dicho valor de la columna 1.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    data_1 = [(line.split("\t")[0], int(line.split("\t")[1])) for line in data]
    letter_aso = {}
    for valor, clave in data_1:
        if clave not in letter_aso:
            letter_aso[clave] = []
        letter_aso[clave].append(valor)
    
    result = [(key,value) for key, value in letter_aso.items()] 
    result = sorted(result)   
        
    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    data_1 = [(line.split("\t")[0], int(line.split("\t")[1])) for line in data]
    letter_aso = {}
    for valor, clave in data_1:
        if clave not in letter_aso:
            letter_aso[clave] = set()
        letter_aso[clave].add(valor)
    
    result = [(key,sorted(list(value))) for key, value in letter_aso.items()] 
    result = sorted(result)   
        
        
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv", "r") as file:
        data = file.readlines()       
    data_1 = [line.split("\t")[4].strip() for line in data]
    data_1 = [elemt.split(",") for elemt in data_1]
    data_1 = [elemt.split(":")[0] for lista in data_1 for elemt in lista]
    sum_letter = {}
    for element in data_1:
        if element in sum_letter:
            sum_letter[element] += 1
        else:
            sum_letter[element] = 1
            
    result = sorted(sum_letter)
    letter = {}
    for element in result:
        letter[element] = sum_letter[element]
        
        
    return letter


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r") as file:
        data = file.readlines()   
    data_1 = [(line.split("\t")[0],line.split("\t")[3],line.split("\t")[4].strip())  for line in data]
    data_1 = [(a, len(b.split(",")), len(c.split(","))) for a,b,c in data_1]
     
    
    return data_1


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    data_1 = [(line.split("\t")[1],line.split("\t")[3])  for line in data]
    data_1 = [(b.split(","), int(a) )  for  a, b in data_1]
    letter = []
    for lista, value in  data_1:
        for key  in lista:
            letter.append((key,value))
    dic_letter = {}
    for key, value in letter:
        if key not in dic_letter:
            dic_letter[key] = value
        else:
            dic_letter[key] = dic_letter[key] + value 
    
    
    result = sorted(dic_letter)
    dic_result = {}
    for key in result:
        dic_result[key] = dic_letter[key]
    
    
      
    return dic_result


def pregunta_12():
    import re
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r") as file:
        data = []
        for line in file:
            data.append(line.split("\t"))
    data_1 = [ (lista[0], lista[4].strip()) for lista  in data]
    data_1 = [ (x, re.findall(r"\d+", y)) for x,y in data_1]
    # data_1 = [(a, b.split(",")) for a,b in data_1]
    values = []
    for key, lista in data_1:
        lista = [int(vlr) for vlr in lista]
        values.append((key, sum(lista)))
    
    dict_key = {}
    for key,value in values:
        if key not in dict_key:
            dict_key[key] = value
        else:
            dict_key[key] = dict_key[key] + value
    
    result = sorted(dict_key)
    dict_resul = dict()
    for key in result:
        dict_resul[key]= dict_key[key]
    
        
    return dict_resul
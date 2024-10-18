"""
Laboratory work №1
Work of Anna Kryvulia and Oksana Moskviak
"""

def read_matrix(file_name):
    """
    Reading a relation(matrix) from a file
    """
    matrix = []
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            row = [int(char) for char in line.strip()]
            matrix.append(row)
    return matrix


def write_file(matrix, output_file):
    """
    Writing a relation(matrix) to a file.
    """
    with open(output_file, 'w', encoding="utf-8") as f:
        for line in matrix:
            line_str = ''.join(str(char) for char in line)
            f.write(line_str + '\n')

def reflexive_closure(file_name):
    """
    Searching symetric closure
    for a given relation in the form of a matrix.
    Returns a matrix that is reflexive.
    """
    matrix = read_matrix(file_name)
    matrix_len = len(matrix)

    for n in range(matrix_len):
        if matrix[n][n] != 1:
            matrix[n][n] = 1
    write_file(matrix, file_name)
    return matrix

def symetric_closure(file_name):
    """
    Searching symetric closure
    for a given relation in the form of a matrix.
    Returns a matrix that is transitive.
    """
    matrix = read_matrix(file_name)
    matrix_len = len(matrix)
    for n in range(matrix_len):
        for el in range(matrix_len):
            if matrix[n][el] != matrix[el][n]:
                matrix[n][el] = 1
                matrix[el][n] = 1
    write_file(matrix, file_name)
    return matrix

def transitive_closure(file_name: str):
    """
    Searching transitive closure
    for a given relation in the form of a matrix 
    according to Warshall's algorithm. Returns a matrix 
    that is transitive.
    """
    matrix = read_matrix(file_name)
    matrix_len = len(matrix)
    matrix_count = 0
    while matrix_count < matrix_len:
        crnt_line = matrix[matrix_count]
        for line in matrix:
            if line[matrix_count] == 1:
                for index, element in enumerate(line):
                    element = element or crnt_line[index]
        matrix_count += 1
    write_file(matrix, file_name)
    return matrix


def find_classes(file_name):
    """
    Breakdown of the equivalence relation into equivalence classes.
    Returns a list of equivalence classes (each class is also a list).
    """
    matrix = read_matrix(file_name)
    matrix_unique = []
    for line in matrix:
        if line not in matrix_unique:
            matrix_unique.append(line)
    res = []
    for row in matrix_unique:
        eqv_class = []
        for index, value in enumerate(row):
            if value == 1:
                eqv_class.append(index+1)
        res.append(eqv_class)
    return res

def check_transitive(file_name):
    """
    Checking if the relation is transitive. 
    Returns a Boolean value (True or False).
    """
    matrix = read_matrix(file_name)
    matrix_transitive = transitive_closure(file_name)
    for index, value in enumerate(matrix):
        if matrix_transitive[index] != value:
            return False
    return True

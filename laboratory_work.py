"""
Laboratory work №1
Work of Anna Kryvulia and Oksana Moskviak
"""
import copy

# Task 1
def read_matrix(file_name: str)-> list[list[int]] | None:
    """
    Reading a relation(matrix) from a file.

    str -> list[list[int]]| None
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w",delete=False) as tmp:
    ...         _= tmp.write('0011\\n1011\\n1010\\n1110')
    >>> read_matrix(tmp.name)
    [[0, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0]]
    """
    if not isinstance(file_name, str):
        return None

    matrix = []

    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            row = [int(char) for char in line.strip()]
            if len(row) != 0:
                matrix.append(row)
        if len(matrix) == 0:
            return None
    return matrix


def write_to_file(matrix: list[list[int]], output_file: str)-> None:
    """
    Writing a relation (matrix) to a file.

    list[list[int]], str -> None
    Creates a file with input from {matrix}
    >>> write_to_file([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], '1.csv')
    >>> with open('1.csv', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    11111
    11111
    11111
    11111
    11111
    """
    if not isinstance(matrix, list) or not isinstance(output_file, str):
        return None
    if '.csv' not in output_file:
        return None

    with open(output_file, 'w', encoding="utf-8") as f:
        for line_in, line in enumerate(matrix):
            line_str = ''.join(str(char) for char in line)
            if line_in != len(matrix) - 1:
                f.write(line_str + '\n')
            else:
                f.write(line_str)

# Task 2
def reflexive_closure(matrix: list[list[int]]) -> list[list[int]] | None:
    """
    Searching symetric closure
    for a given relation in the form of a matrix.
    Returns a matrix that is reflexive.
    
    list[list[int]]-> list[list[int]] | None
    >>> matrix = [[0, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0]]
    >>> reflexive_closure(matrix)
    [[1, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1]]

    str -> list[list[int]] | None
    """
    if not isinstance(matrix, list):
        return None

    matrix_len = len(matrix)

    for n in range(matrix_len):
        if matrix[n][n] != 1:
            matrix[n][n] = 1

    return matrix

def symetric_closure(matrix: list[list[int]]) -> list[list[int]] | None:
    """
    Searching symetric closure
    for a given relation in the form of a matrix.
    Returns a matrix that is transitive.

    list[list[int]]-> list[list[int]] | None
    >>> matrix = [[1, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1]]
    >>> symetric_closure(matrix)
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    """
    if not isinstance(matrix, list):
        return None

    matrix_len = len(matrix)

    for n in range(matrix_len):
        for el in range(matrix_len):
            if matrix[n][el] != matrix[el][n]:
                matrix[n][el] = 1
                matrix[el][n] = 1
    return matrix

# Task 3
def transitive_closure(matrix: list[list[int]]) -> list[list[int]]:
    """
    Searching transitive closure
    for a given relation in the form of a matrix 
    according to Warshall's algorithm. Returns a matrix 
    that is transitive.

    str -> list[list] | None

    >>> transitive_closure([[0, 1, 1, 0],[0, 1, 0, 1],[0, 0, 0, 0],[0, 0, 0, 0]])
    [[0, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> transitive_closure([[0, 1, 1, 0, 1], [1, 0, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0]])
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0]]
    """
    matrix_len = len(matrix)
    matrix_count = 0

    while matrix_count < matrix_len:
        crnt_line = matrix[matrix_count]
        for line in matrix:
            if line[matrix_count] == 1:
                for index, element in enumerate(line):
                    line[index] = element or crnt_line[index]
        matrix_count += 1
    return matrix

# Task 4
def find_classes(matrix: list[list[int]]) -> list[list[int]]:
    """
    Breakdown of the equivalence relation into equivalence classes.
    Returns a list of equivalence classes (each class is also a list).

    str -> list[list] | None

    >>> matrix = [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1]]
    >>> find_classes(matrix)
    [[1, 2, 4], [3]]
    """
    matrix_unique = []

    for line in matrix:
        if line not in matrix_unique:
            matrix_unique.append(line)
    all_classes= []
    for row in matrix_unique:
        eqv_class = []
        for index, value in enumerate(row):
            if value == 1:
                eqv_class.append(index + 1)
        all_classes.append(eqv_class)
    return all_classes

# Task 5
def check_transitive(matrix: list[list[int]]) -> bool | None:
    """
    Checking if the relation is transitive. 
    Returns a Boolean value (True or False).

    str -> bool | None


    >>> check_transitive([[1, 0, 1, 1, 0], [0, 1, 0, 1, 1], [1, 0, 1, 1, 0], \
        [1, 1, 1, 1, 0], [0, 1, 0, 0, 1]])
    False
    >>> check_transitive([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0]])
    True
    """
    matrix_to_check = copy.deepcopy(matrix)
    transitive_matrix = transitive_closure(matrix)
    for row_in, row in enumerate(matrix_to_check):
        for element_in, element in enumerate(row):
            if element != transitive_matrix[row_in][element_in]:
                return False
    return True



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

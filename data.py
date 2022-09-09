import random

def get_data():
    my_array = [[8,5,4,12],
                [2,6,3,9],
                [1,2,3,4],
                [5,3,4,6],
                [2,2,3,4],
                [2,4,3,4],
                [3,2,6,1],
                [1,5,1,3]]

    dx = 4
    dy = 8
    matrix = [[0 for x in range(dx)] for y in range(dy)]

    for i in range(8):
        for j in range(4):
            a = random.randint(0, 20)
            matrix[i][j] = a

    # return matrix
    return my_array
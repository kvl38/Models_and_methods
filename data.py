import random
#Задача 1.
def get_data():
    my_array = [[8,5,4,12],
                [2,6,3,9],
                [1,2,3,4],
                [5,3,4,6],
                [2,2,3,4],
                [2,4,3,4],
                [3,2,6,1],
                [1,5,1,3]]
    return my_array

#Задача 2.
def get_data_pr2():
    my_array_pr2 = [[[8, 2], [5, 2], [4, 3], [12, 4]],
                [[2, 2], [6, 4], [3, 3], [9, 4]],
                [[1, 3], [2, 2], [3, 6], [4, 1]],
                [[5, 1], [3, 5], [4, 1], [6, 3]],
                [[2, 3], [2, 6], [3, 4], [4, 10]],
                [[2, 9], [4, 7], [3, 5], [4, 11]],
                [[3, 4], [2, 5], [6, 6], [1, 12]],
                [[1, 7], [5, 8], [1, 9], [3, 13]]]
    return my_array_pr2


def get_random_data():
    dx = 4
    dy = 8
    matrix = [[0 for x in range(dx)] for y in range(dy)]

    for i in range(8):
        for j in range(4):
            a = random.randint(0, 20)
            matrix[i][j] = a
    return matrix

#Задача №1
import data

def index(arr, num):
    array_of_indice = []
    for i, x in enumerate(arr):
        if x == num:
            array_of_indice.append(i+1)
    return array_of_indice

def x_index(arr, number):
    interval = index(arr, number)
    if len(interval) == 1:
        print(f"Оптимальное решение по критерию: x{interval[0]}")
    else:
        for i in interval:
            print(f"Оптимальное решение по критерию: x{i}")
    intermediate_result = []
    for it in range(1, 9):
        if it in interval: intermediate_result.append(1)
        else: intermediate_result.append(0)
    result.append(intermediate_result)

#1.Критерий Вальда
def Valdo(arr):
    min_array_element = []
    for i in arr:
        min_element = i[0]
        for j in i:
            if min_element > j:min_element = j
        min_array_element.append(min_element)
    print("Минимальные значениея массива A:", min_array_element)
    print("Максимальный элемент по столбцу: ", max(min_array_element))
    x_index(min_array_element, max(min_array_element))

#2.КритериЙ Сэвиджа
def Savage(arr):
    b = []
    for j in range(4):
        max_array_element = arr[0][j]
        for i in arr:
            if max_array_element < i[j]:
                max_array_element = i[j]
        b.append(max_array_element)
    print("b = ", b)

    for k in range(4):
        for i in range(8):
            arr[i][k] = b[k] - arr[i][k]
    print("Новый массив:", arr)

    b_max = []
    for i in arr:
        b_max.append(max(i))
    print("b_max = ", b_max)
    x_index(b_max, min(b_max))

#3.Критерий Гурвица ( y=0.6 )
def Hurwitz(arr):
    y = 0.6
    array_of_minima = []
    array_of_maxima = []
    g = []
    for i in arr:
        array_of_minima.append(min(i))
        array_of_maxima.append(max(i))
    for j in range(8):
        expression = round(y * array_of_minima[j] + (1 - y) * array_of_maxima[j], 2)
        g.append(expression)
    print("array_of_minima:", array_of_minima)
    print("array_of_maxima", array_of_maxima)
    print("G:", g)
    x_index(g, max(g))

#4.Критерий Байеса (p=[0,1; 0,4; 0,4; 0,1])
def Bayes(arr):
    d = []
    for i in arr: d.append(round(i[0] * 0.1 + i[1] * 0.4 + i[2] * 0.4 + i[3] * 0.1, 2))
    max_element = max(d)
    print("di:", d)
    x_index(d, max_element)

#5.Критерий Лапласа
def Laplas(arr):
    n = 4
    f = []
    for i in arr:
        sum = 0
        for j in range(4):
            sum += i[j]
        f.append((1/n) * sum)
    print("fi:", f)
    x_index(f, max(f))

def Final_count(arr):
    intermediate_final_result = []
    for j in range(8):
        sum = 0
        for i in arr:
            if i[j] == 1:sum += 1
        intermediate_final_result.append(sum)
    result.append(intermediate_final_result)

if __name__ == '__main__':
    initial_array = data.get_data()
    result = []
    print("Начальный массив данных: ", data.get_data())
    print("\n1.Критерий Вальда")
    Valdo(initial_array)
    print("\n2.КритериЙ Сэвиджа")
    Savage(initial_array)
    print("\n3.Критерий Гурвица ( y=0.6 )")
    Hurwitz(data.get_data())
    print("\n4.Критерий Байеса (p=[0,1; 0,4; 0,4; 0,1])")
    Bayes(data.get_data())
    print("\n5.Критерий Лапласа")
    Laplas(data.get_data())
    Final_count(result)

    import pandas as pd
    df = pd.DataFrame(result).T
    df.rename(columns={0: 'Вальда', 1: 'Сэвиджа', 2: 'Гурвица', 3: 'Байеса', 4: 'Лапласа', 5: "Результат"}, inplace=True)
    df = df.rename(index={0: 'x1', 1: 'x2', 2: 'x3', 3: 'x4', 4: 'x5', 5: 'x6', 6: 'x7', 7: 'x8'})
    print("\n\t\t\t\t\tМатрица голосования\n", df)

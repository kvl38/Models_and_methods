import data
from data import get_data_pr2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

overall_result = []

def xy_index(arr, elements):
    interval = [0] * 8
    it = 0
    i = 0
    while it != 8:
        if elements[i] == arr[it]:
            interval[it] = 1
            i+=1
        it+=1
    overall_result.append(interval)

    for element in elements:
        for i, k in enumerate(arr):
            if element == k:
                print(f"Оптимальное решение по критерию: x{i+1}")

#1. Принцип векторного максимина
print("\n1. Принцип векторного максимина")
my_array = get_data_pr2()
new_array = []
intermediate_array = []
for i in my_array:
    min1 = i[0][0]
    min2 = i[0][1]
    for j in i:
        if j[0] < min1: min1 = j[0]
        if j[1] < min2: min2 = j[1]
    new_array.append([min1, min2])
print("Множество точек «крайнего пессимизма»: ", new_array)

x = []
y = []
for a in new_array:
    x.append(a[0])
    y.append(a[1])

red_dots = []
for dot in new_array:
    current_x = dot[0]
    current_y = dot[1]
    for k in new_array:
        if current_x <= k[0] and current_y <= k[1]:
            current_x = k[0]
            current_y = k[1]
    if current_x == dot[0] and current_y == dot[1]:
        red_dots.append([current_x, current_y])
print("Оптимальные решения удовлетворяющие принципу векторного максимина:", red_dots)

xy_index(new_array, red_dots)

x_max = []
y_max = []
for i in red_dots:
    x_max.append(i[0])
    y_max.append(i[1])

plt.suptitle("Задание №1")
plt.scatter(x, y)
plt.scatter(x_max, y_max, c='r')
for it in range(1, 9):
    plt.annotate(f'x{it}', xy=(new_array[it-1][0], new_array[it-1][1]))
plt.grid(True)
plt.show()


#2. Принцип векторного минимаксного сожаления
print("\n2. Принцип векторного минимаксного сожаления")
my_array = get_data_pr2()
perfect_points = []
for i in range(4):
    x_minimax = my_array[0][i][0]
    y_minimax = my_array[0][i][1]
    for k in my_array:
        if x_minimax < k[i][0]: x_minimax = k[i][0]
        if y_minimax < k[i][1]: y_minimax = k[i][1]

    perfect_points.append([x_minimax, y_minimax])
print("Множество «идеальных точек»: ", perfect_points)

for i in range(8):
    for j in range(4):
        my_array[i][j][0] = perfect_points[j][0] - my_array[i][j][0]
        my_array[i][j][1] = perfect_points[j][1] - my_array[i][j][1]

df = pd.DataFrame(my_array)
df.rename(columns={0: 'z1', 1: 'z2', 2: 'z3', 3: 'z4'}, inplace=True)
df.rename(index={0: 'x1', 1: 'x2', 2: 'x3', 3: 'x4', 4: 'x5', 5: 'x6', 6: 'x7', 7: 'x8'}, inplace=True)
print("\nТаблица значений функции векторных рисков:\n", df)

new_array = []
intermediate_array = []
for i in my_array:
    min1 = i[0][0]
    min2 = i[0][1]
    for j in i:
        if j[0] > min1: min1 = j[0]
        if j[1] > min2: min2 = j[1]
    new_array.append([min1, min2])
print("Множество точек «крайнего пессимизма»: ", new_array)

x = []
y = []
for a in new_array:
    x.append(a[0])
    y.append(a[1])

red_dots = []
for dot in new_array:
    current_x = dot[0]
    current_y = dot[1]
    for k in new_array:
        if current_x >= k[0] and current_y >= k[1]:
            current_x = k[0]
            current_y = k[1]
    if current_x == dot[0] and current_y == dot[1]:
        red_dots.append([current_x, current_y])
print("Оптимальные решения удовлетворяющие принципу векторного минимаксного сожаления :", red_dots)
print(xy_index(new_array, red_dots))
x_max = []
y_max = []
for i in red_dots:
    x_max.append(i[0])
    y_max.append(i[1])


plt.suptitle("Задание №2")
plt.scatter(x, y)
plt.scatter(x_max, y_max, c='r')
for it in range(1, 9):
    plt.annotate(f'x{it}', xy=(new_array[it-1][0], new_array[it-1][1]))
plt.grid(True)
plt.show()


#3. Функции
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

#4.Критерий Лапласа
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

#5. Сумма очков голосования по проектам
def Final_count(arr):
    intermediate_final_result = []
    for j in range(8):
        sum = 0
        for i in arr:
            if i[j] == 1:sum += 1
        intermediate_final_result.append(sum)
    result.append(intermediate_final_result)


#3. Принципы Вальда, Сэвиджа, Гурвица, Лапласа для f1
print("\n3. Принципы Вальда, Сэвиджа, Гурвица, Лапласа для f1:")

def new_f1():
    f1 = []
    my_array = get_data_pr2()
    for i in my_array:
        intermediate_array = []
        for j in range(4):
            intermediate_array.append(i[j][0])
        f1.append(intermediate_array)
        del intermediate_array
    return f1

df1 = pd.DataFrame(new_f1())
df1.rename(columns={0: 'z1', 1: 'z2', 2: 'z3', 3: 'z4'}, inplace=True)
df1.rename(index={0: 'x1', 1: 'x2', 2: 'x3', 3: 'x4', 4: 'x5', 5: 'x6', 6: 'x7', 7: 'x8'}, inplace=True)
print("\tТаблица Q для f1 \n", df1)

result = []
print("\n3.1.Критерий Вальда")
Valdo(new_f1())
print("\n3.2.КритериЙ Сэвиджа")
Savage(new_f1())
print("\n3.3.Критерий Гурвица ( y=0.6 )")
Hurwitz(new_f1())
print("\n3.4.Критерий Лапласа")
Laplas(new_f1())
id1 = index(result[-1], max(result[-1]))[0]
del result
res1 = [0] * 8
res1[id1-1] = 1
overall_result.append(res1)


#4. Принципы Вальда, Сэвиджа, Гурвица, Лапласа для f2
print("\n4. Принципы Вальда, Сэвиджа, Гурвица, Лапласа для f2:")

def new_f2():
    f2 = []
    my_array = get_data_pr2()
    for i in my_array:
        intermediate_array = []
        for j in range(4):
            intermediate_array.append(i[j][1])
        f2.append(intermediate_array)
        del intermediate_array
    return f2

df2 = pd.DataFrame(new_f2())
df2.rename(columns={0: 'z1', 1: 'z2', 2: 'z3', 3: 'z4'}, inplace=True)
df2.rename(index={0: 'x1', 1: 'x2', 2: 'x3', 3: 'x4', 4: 'x5', 5: 'x6', 6: 'x7', 7: 'x8'}, inplace=True)
print("\tТаблица Q для f2 \n", df2)

result = []
print("\n4.1.Критерий Вальда")
Valdo(new_f2())
print("\n4.2.КритериЙ Сэвиджа")
Savage(new_f2())
print("\n4.3.Критерий Гурвица ( y=0.6 )")
Hurwitz(new_f2())
print("\n4.4.Критерий Лапласа")
Laplas(new_f2())
id2 = index(result[-1], max(result[-1]))[0]
del result
res2 = [0] * 8
res2[id2-1] = 1
overall_result.append(res2)

#5. Матрица голосования
def Final_count(arr):
    intermediate_final_result = []
    for j in range(8):
        sum = 0
        for i in arr:
            if i[j] == 1:sum += 1
        intermediate_final_result.append(sum)
    overall_result.append(intermediate_final_result)

Final_count(overall_result)
df = pd.DataFrame(overall_result).T
df.rename(columns={0: 'вект. максимин', 1: 'вект. минимакс сож.', 2: 'f1', 3: 'f2', 4: 'Результат'}, inplace=True)
df.rename(index={0: 'x1', 1: 'x2', 2: 'x3', 3: 'x4', 4: 'x5', 5: 'x6', 6: 'x7', 7: 'x8'},inplace=True)
print("\n\t\t\t\t\t5. Матрица голосования\n", df)



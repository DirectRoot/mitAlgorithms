from insertionSort import *
from mergeSort import *
import random
import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

dataLength = 10
dataRange = 10000
data = []

while len(data) < 1000000:
    data = []
    for i in range(dataLength):
        data.append(random.randrange(dataRange))

    if len(data) < 40000:
        wrapped = wrapper(insertionSort, data)
        print "{0} (insertionSort {1})".format(timeit.timeit(wrapped, number=1), len(data))

    wrapped = wrapper(mergeSort, data)
    print "{0} (mergeSort {1})\n".format(timeit.timeit(wrapped, number=1), len(data))

    dataLength = dataLength * 2

'''
2.59876251221e-05 (insertionSort 10)
5.19752502441e-05 (mergeSort 10)

5.19752502441e-05 (insertionSort 20)
0.000125885009766 (mergeSort 20)

0.000182867050171 (insertionSort 40)
0.000211954116821 (mergeSort 40)

0.000684976577759 (insertionSort 80)
0.000440835952759 (mergeSort 80)

0.00332999229431 (insertionSort 160)
0.00110101699829 (mergeSort 160)

0.0128479003906 (insertionSort 320)
0.00398898124695 (mergeSort 320)

0.0750849246979 (insertionSort 640)
0.0047619342804 (mergeSort 640)

0.367293119431 (insertionSort 1280)
0.0113608837128 (mergeSort 1280)

0.994287014008 (insertionSort 2560)
0.0264420509338 (mergeSort 2560)

3.65390205383 (insertionSort 5120)
0.0554151535034 (mergeSort 5120)

14.8469190598 (insertionSort 10240)
0.109691143036 (mergeSort 10240)

57.5089609623 (insertionSort 20480)
0.160472869873 (mergeSort 20480)

0.337938070297 (mergeSort 40960)

0.731607913971 (mergeSort 81920)

2.04046607018 (mergeSort 163840)

4.89412689209 (mergeSort 327680)

6.39935898781 (mergeSort 655360)

13.9483931065 (mergeSort 1310720)
'''
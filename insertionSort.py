def insertionSort(data):
    # step along list
    # if element x at point i smaller than y at i-1, swap x and y
    # repeat for x until larger than element at i-1

    for key in range(len(data)):
        i = key
        while data[i] < data[i-1] and i > 0: # if i == 0 then we're at the start of the data
            data[i-1], data[i] = data[i], data[i-1]
            i = i-1

    return data

'''
import random

data = []
for i in range(1000):
    data.append(random.randrange(1000))

print data
print insertionSort(data)
'''
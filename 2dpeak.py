
def findAPeak(data):

    result = -1

    for i in range(len(data)):

        # if first element and it's >= to the second, we've found a peak!
        if i == 0 and data[i] >= data[i + 1]:
            result = i
            break

        # if it's the last element and it's >= than the previous, it's a peak
        elif i == len(data) - 1 and data[i] >= data[i - 1]:
            result = i
            break

        # if it's any other element, and it's bigger than those either side, then it's a peak
        elif data[i] >= data[i - 1] and data[i] >= data[i + 1]:
            result = i
            break

    return result


def findAPeakBetter(data, nextIndex=None, depth = 1):
    rightIsBigger = False
    leftIsBigger = False
    n = len(data)

    # figure out the mid point, if we weren't given the next index to try
    if nextIndex == None:
        if n == 1:
            return 0
        else:
            i = n / 2
    else:
        i = nextIndex

    print i
    #print depth

    # if first element and it's >= to the second, we've found a peak
    if i == 0 and data[i] >= data[i + 1]:
        return i

    # if it's the last element and it's >= than the previous, it's a peak
    elif i == len(data) - 1 and data[i] >= data[i - 1]:
        return i

    # find out if the element to the right is bigger then n[i]
    elif data[i] <= data[i + 1]:
        rightIsBigger = True

    # find out if the element to the left is bigger than n[i] (if the one to right isn't)
    elif data[i] <= data[i - 1]:
        leftIsBigger = True

    # if we found the left side is bigger, go that way by picking the mid point of that half
    if leftIsBigger:
        depth += 1
        offset = (n / 2 ** depth)
        if offset == 0: offset = 1
        nextIndex = i - offset

        return findAPeakBetter(data, nextIndex, depth)

    # if we found the right side is bigger, go that way!
    elif rightIsBigger:
        depth += 1
        offset = (n / 2 ** depth)
        if offset == 0: offset = 1
        nextIndex = i + offset
        return findAPeakBetter(data, nextIndex, depth)

    # if neither side was bigger, then we found a peak
    else:
        return i


findAPeakBetter([1, 2, 3, 4, 5, 4, 5, 4, 3, 2])

'''
# testing the two 2D peak finding algorithms
import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

dataLength = 10
data = []

while len(data) < 100000000:
    data = []
    for i in range(dataLength):
        data.append(i)

    wrapped = wrapper(findAPeak, data)
    print "{0} (findAPeak {1})".format(timeit.timeit(wrapped, number=1), len(data))

    wrapped = wrapper(findAPeakBetter, data)
    print "{0} (findAPeakBetter {1})\n".format(timeit.timeit(wrapped, number=1), len(data))

    dataLength = dataLength * 10


8.82148742676e-06 (findAPeak 10)
4.98294830322e-05 (findAPeakBetter 10)

2.78949737549e-05 (findAPeak 100)
1.00135803223e-05 (findAPeakBetter 100)

0.000277996063232 (findAPeak 1000)
1.69277191162e-05 (findAPeakBetter 1000)

0.00325894355774 (findAPeak 10000)
2.28881835938e-05 (findAPeakBetter 10000)

0.0410571098328 (findAPeak 100000)
3.00407409668e-05 (findAPeakBetter 100000)

0.294404983521 (findAPeak 1000000)
5.48362731934e-05 (findAPeakBetter 1000000)

2.89510893822 (findAPeak 10000000)
4.2200088501e-05 (findAPeakBetter 10000000)

29.64407897 (findAPeak 100000000)
5.79357147217e-05 (findAPeakBetter 100000000)
'''
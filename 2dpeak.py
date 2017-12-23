
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


def findAPeakBetter(data, nextIndex=None):
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
        nextIndex = i / 2
        return findAPeakBetter(data, nextIndex)

    # if we found the right side is bigger, go that way!
    elif rightIsBigger:
        nextIndex = i + int((n - i) / 2)
        return findAPeakBetter(data, nextIndex)

    # if neither side was bigger, then we found a peak
    else:
        return i


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

'''
1.00135803223e-05 (findAPeak 10)
1.69277191162e-05 (findAPeakBetter 10)

2.88486480713e-05 (findAPeak 100)
1.19209289551e-05 (findAPeakBetter 100)

0.000272035598755 (findAPeak 1000)
1.50203704834e-05 (findAPeakBetter 1000)

0.00370693206787 (findAPeak 10000)
2.28881835938e-05 (findAPeakBetter 10000)

0.0607008934021 (findAPeak 100000)
2.78949737549e-05 (findAPeakBetter 100000)

0.420443058014 (findAPeak 1000000)
4.6968460083e-05 (findAPeakBetter 1000000)

3.28927111626 (findAPeak 10000000)
3.91006469727e-05 (findAPeakBetter 10000000)

36.6545820236 (findAPeak 100000000)
7.10487365723e-05 (findAPeakBetter 100000000)
'''
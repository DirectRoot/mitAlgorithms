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
        print "{0} (insertionSort - random {1})".format(timeit.timeit(wrapped, number=1), len(data))

    wrapped = wrapper(mergeSort, data)
    print "{0} (mergeSort - random {1})\n".format(timeit.timeit(wrapped, number=1), len(data))

    dataLength = dataLength * 2


dataLength = 10
data = []

while len(data) < 1000000:
    data = []
    for i in reversed(range(dataLength)):
        data.append(i)

    if len(data) < 40000:
        wrapped = wrapper(insertionSort, data)
        print "{0} (insertionSort - reversed {1})".format(timeit.timeit(wrapped, number=1), len(data))

    wrapped = wrapper(mergeSort, data)
    print "{0} (mergeSort - reversed {1})\n".format(timeit.timeit(wrapped, number=1), len(data))

    dataLength = dataLength * 2


dataLength = 10
data = []

while len(data) < 1000000:
    data = []
    for i in range(dataLength):
        data.append(i)

        if i == dataLength / 2:
            data[i], data[i-1] = data[i-1], data[i]


    wrapped = wrapper(insertionSort, data)
    print "{0} (insertionSort - almost {1})".format(timeit.timeit(wrapped, number=1), len(data))

    wrapped = wrapper(mergeSort, data)
    print "{0} (mergeSort - almost {1})\n".format(timeit.timeit(wrapped, number=1), len(data))

    dataLength = dataLength * 2

'''
1.81198120117e-05 (insertionSort - random 10)
3.00407409668e-05 (mergeSort - random 10)

3.00407409668e-05 (insertionSort - random 20)
5.60283660889e-05 (mergeSort - random 20)

9.60826873779e-05 (insertionSort - random 40)
0.000102043151855 (mergeSort - random 40)

0.000379085540771 (insertionSort - random 80)
0.000306844711304 (mergeSort - random 80)

0.00185322761536 (insertionSort - random 160)
0.000479936599731 (mergeSort - random 160)

0.00633811950684 (insertionSort - random 320)
0.00105500221252 (mergeSort - random 320)

0.0553789138794 (insertionSort - random 640)
0.00236010551453 (mergeSort - random 640)

0.135864973068 (insertionSort - random 1280)
0.00471496582031 (mergeSort - random 1280)

0.517333030701 (insertionSort - random 2560)
0.0102369785309 (mergeSort - random 2560)

1.68004703522 (insertionSort - random 5120)
0.0243289470673 (mergeSort - random 5120)

6.71475315094 (insertionSort - random 10240)
0.0473551750183 (mergeSort - random 10240)

26.7186670303 (insertionSort - random 20480)
0.0996949672699 (mergeSort - random 20480)

0.279405117035 (mergeSort - random 40960)

0.526700019836 (mergeSort - random 81920)

1.13886499405 (mergeSort - random 163840)

2.41994714737 (mergeSort - random 327680)

5.15513110161 (mergeSort - random 655360)

10.8998730183 (mergeSort - random 1310720)

2.31266021729e-05 (insertionSort - reversed 10)
2.90870666504e-05 (mergeSort - reversed 10)

5.19752502441e-05 (insertionSort - reversed 20)
4.81605529785e-05 (mergeSort - reversed 20)

0.000209093093872 (insertionSort - reversed 40)
9.98973846436e-05 (mergeSort - reversed 40)

0.000874042510986 (insertionSort - reversed 80)
0.000217914581299 (mergeSort - reversed 80)

0.00302386283875 (insertionSort - reversed 160)
0.000503063201904 (mergeSort - reversed 160)

0.012079000473 (insertionSort - reversed 320)
0.0010290145874 (mergeSort - reversed 320)

0.0518579483032 (insertionSort - reversed 640)
0.00224590301514 (mergeSort - reversed 640)

0.224770069122 (insertionSort - reversed 1280)
0.00618505477905 (mergeSort - reversed 1280)

0.945399045944 (insertionSort - reversed 2560)
0.0106310844421 (mergeSort - reversed 2560)

3.7645740509 (insertionSort - reversed 5120)
0.0237300395966 (mergeSort - reversed 5120)

16.5248389244 (insertionSort - reversed 10240)
0.0494980812073 (mergeSort - reversed 10240)

69.151499033 (insertionSort - reversed 20480)
0.108503103256 (mergeSort - reversed 20480)

0.246942043304 (mergeSort - reversed 40960)

0.510613203049 (mergeSort - reversed 81920)

1.12321400642 (mergeSort - reversed 163840)

2.35252404213 (mergeSort - reversed 327680)

4.77089810371 (mergeSort - reversed 655360)

10.2568678856 (mergeSort - reversed 1310720)

1.00135803223e-05 (insertionSort - almost 10)
2.8133392334e-05 (mergeSort - almost 10)

6.91413879395e-06 (insertionSort - almost 20)
4.81605529785e-05 (mergeSort - almost 20)

8.10623168945e-06 (insertionSort - almost 40)
9.89437103271e-05 (mergeSort - almost 40)

1.19209289551e-05 (insertionSort - almost 80)
0.000272035598755 (mergeSort - almost 80)

2.19345092773e-05 (insertionSort - almost 160)
0.00047492980957 (mergeSort - almost 160)

4.60147857666e-05 (insertionSort - almost 320)
0.00112199783325 (mergeSort - almost 320)

0.000140905380249 (insertionSort - almost 640)
0.00232601165771 (mergeSort - almost 640)

0.000292062759399 (insertionSort - almost 1280)
0.00488996505737 (mergeSort - almost 1280)

0.000646829605103 (insertionSort - almost 2560)
0.0103051662445 (mergeSort - almost 2560)

0.00139498710632 (insertionSort - almost 5120)
0.0219089984894 (mergeSort - almost 5120)

0.00295400619507 (insertionSort - almost 10240)
0.0492558479309 (mergeSort - almost 10240)

0.00703811645508 (insertionSort - almost 20480)
0.127825975418 (mergeSort - almost 20480)

0.0162260532379 (insertionSort - almost 40960)
0.232527971268 (mergeSort - almost 40960)

0.0317440032959 (insertionSort - almost 81920)
0.483777999878 (mergeSort - almost 81920)

0.0647690296173 (insertionSort - almost 163840)
1.03313612938 (mergeSort - almost 163840)

0.127212047577 (insertionSort - almost 327680)
2.17325496674 (mergeSort - almost 327680)

0.238681077957 (insertionSort - almost 655360)
4.48832178116 (mergeSort - almost 655360)

0.448536872864 (insertionSort - almost 1310720)
9.3025598526 (mergeSort - almost 1310720)
'''
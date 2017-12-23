# based on...
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

def mergeSort(data, calls=0):
    calls += 1
    #print "call: " + str(calls)
    #print str(data) + "\n"

    # a 1 element list is the base case, so we stop the recursion
    if len(data) > 1:

        # otherwise, keep splitting the list into two halves
        mid = len(data) / 2
        leftHalf = data[:mid]
        rightHalf = data[mid:]

        calls = mergeSort(leftHalf, calls)
        calls = mergeSort(rightHalf, calls)

        # setting up our index pointers, one for each half and
        # one for the data that this call is rearranging
        leftIndex=0
        rightIndex=0
        dataIndex=0

        # while there's elements in both left and right halves, that haven't been
        # put back into the data list
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):

            # if the next element in the left half is smaller than that on the right,
            # put that element in the next space within the data list
            if leftHalf[leftIndex] < rightHalf[rightIndex]:
                data[dataIndex]=leftHalf[leftIndex]
                leftIndex=leftIndex+1

            # otherwise put the next element from the right half into the next space
            # in the data list
            else:
                data[dataIndex]=rightHalf[rightIndex]
                rightIndex=rightIndex+1
            dataIndex=dataIndex+1

        # if all the elements from the right half have been used, this ensures
        # the remaining elements from the left make it back into the data list
        while leftIndex < len(leftHalf):
            data[dataIndex]=leftHalf[leftIndex]
            leftIndex=leftIndex+1
            dataIndex=dataIndex+1

        # this does the same as above, but for when the left half is exhausted
        # and there's still unused elements in the right
        while rightIndex < len(rightHalf):
            data[dataIndex]=rightHalf[rightIndex]
            rightIndex=rightIndex+1
            dataIndex=dataIndex+1


    return calls

'''
alist = [54,26,93,17,77,31,44,55,20]
calls = mergeSort(alist)
print(alist)
'''
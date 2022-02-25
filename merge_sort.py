import numpy as np

def merging(ar, left, right, mid):
    temp = [0] * ((right - left) + 1)
    tempIndex = 0
    leftIndex = left
    rightIndex = mid + 1

    while leftIndex <= mid and rightIndex <= right:
        if ar[leftIndex] < ar[rightIndex]:
            temp[tempIndex] = ar[leftIndex]
            leftIndex += 1
        else:
            temp[tempIndex] = ar[rightIndex]
            rightIndex += 1
        tempIndex += 1

    while leftIndex <= mid:
        temp[tempIndex] = ar[leftIndex];
        tempIndex += 1
        leftIndex += 1

    while rightIndex <= right:
        temp[tempIndex] = ar[rightIndex]
        tempIndex += 1
        rightIndex += 1

    tempIndex = 0

    for i in range(left, right + 1):
        ar[i] = temp[tempIndex]
        tempIndex += 1
@profile
def MergeSort(ar, begin, end):
    if begin != end:
        mid = (end + begin) // 2
        afterMid = mid + 1
        MergeSort(ar, begin, mid)
        MergeSort(ar, afterMid, end)
        merging(ar, begin, end, mid)

def generateList(lowerBound, upperBound, step=1):
    ints = np.arange(lowerBound, upperBound + 1, step)
    np.random.shuffle(ints)
    return ints

def swap(a, i, j): #a is the array swap the value in j and k
    t = a[i]
    a[i] = a[j]
    a[j] = t

@profile
def SelectionSort(arr):
    size = len(arr)
    for i in range(size):
        #find the smallest item in range i to n
        k = i # k hold the index of the smallest number
        for j in range(i + 1, size):
            if arr[k] > arr[j]:
                k = j
        swap(arr, i, k)

    return arr

@profile
def InsertionSort(A):
    for i in range(1, len(A)):
        k = i
        v = A[k]
        while k > 0 and A[k - 1] > v:
            swap(A, k - 1, k)
            k -= 1

    return A

@profile
def BubbleSort(A):
    for i in range(len(A) - 1):
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

    return A

Arr1 = generateList(1, 1000)
Arr2 = Arr1.copy()
Arr3 = Arr1.copy()
Arr4 = Arr1.copy()

#print("Arr1 is ", Arr1)
#print("Arr2 is ", Arr2)
#print("Arr3 is ", Arr3)
#print("Arr4 is ", Arr4)

SelectionSort(Arr1)
InsertionSort(Arr2)
BubbleSort(Arr3)
MergeSort(Arr4, 0, len(Arr4) - 1)

#print("Sorted")
#print("________________________________")

#print("Arr1 is ", Arr1)
#print("Arr2 is ", Arr2)
#print("Arr3 is ", Arr3)
#print("Arr4 is ", Arr4)

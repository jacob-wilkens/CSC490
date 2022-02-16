import numpy as np

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

A = generateList(1, 10000)
#print(A)
SelectionSort(A)
InsertionSort(A)
BubbleSort(A)

import random
import collections
import numpy
import sys

class utility:
    def __init__(self):
        pass

    def generateTestArray(self, maxRange):
        a = list(range(1, maxRange))
        duplicate = random.randint(1, maxRange - 1)
        a.append(duplicate)
        random.shuffle(a)
        return a

#@profile
def SCAN(a):
    size = len(a)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if a[i] == a[j]:
                print("i is ", i, "," "j is ", j)
                print("The duplicate is ", a[i])
                return

@profile
def STOR(a):
    size = len(a)
    b = [0] * size

    print("The size of list a is ", sys.getsizeof(1) * len(a), " in bytes")
    print("The size of list b is ", sys.getsizeof(1) * len(b), " in bytes")

    for i in range(size):
        if b[a[i]] == 1:
            print("The index is", i)
            print("The duplicate is", a[i])
            return
        else:
            b[a[i]] = 1

@profile
def STOR_numpy(a):
    size = len(a)
    d = numpy.zeros(size)

    print("The size of list a is ", sys.getsizeof(1) * len(a), " in bytes")
    print("Memory size of numpy array d in bytes is ", d.itemsize * d.size)

    for i in range(size):
        if d[a[i]] == 1:
            print("The index is", i)
            print("The duplicate is", a[i])
            return
        else:
            d[a[i]] = 1

maxRange = 2000000
array_a = utility().generateTestArray(maxRange)
#SCAN(array_a)
STOR(array_a)
STOR_numpy(array_a)

#Checking Functions work
#print("This is for testing purposes")
#print([item for item, count in collections.Counter(array_a).items() if count > 1])

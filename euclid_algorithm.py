import timeit

# Recursive Function to return gcd of m and n
@profile
def gcdRecursive(m, n):
    if m == 0:
        return n

    return gcdRecursive(n % m, m)

# While Loop Function to return gcd of m and n
@profile
def gcdLoop(m, n):
    while m != 0:
        l = m
        m = n % m
        n = l
    return n

#def testLoop():
    #gcdLoop(190283091283012938, 1293801298)

#def testRecursion():
    #gcdRecursive(190283091283012938, 1293801298)

#Implementation
m = 190283091283012938
n = 1293801298

#Profiler Implementation
gcdLoop(m, n)
gcdRecursive(m, n)

#Time It
#print(timeit.Timer(testLoop).timeit(number=100))
#print(timeit.Timer(testRecursion).timeit(number=100))

#Output
#print("gcd(", m, ",", n, ") = ", gcdRecursive(m, n))
#print("gcd(", m, ",", n, ") = ", gcdLoop(m, n))

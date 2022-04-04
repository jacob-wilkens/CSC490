def calcRedundantBits(m):
    for i in range(m):
        if (2 ** i >= m + i + 1):
            return i

def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)

def decode(bin_data):
    str_data = ''
    for i in range(0, len(bin_data), 7):
        temp_data = int(bin_data[i:i + 7])
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    return str_data

def posRedundantBits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''

    for i in range(1, m + r + 1):
        if (i == 2 ** j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    return res[::-1]

def calcParityBits(arr, r):
    n = len(arr)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            if (j & (2 ** i) == (2 ** i)):
                val = val ^ int(arr[-1 * j])

        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr

def detectError(arr, nr):
    n = len(arr)
    res = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if (j & (2 ** i) == (2 ** i)):
                val = val ^ int(arr[-1 * j])

        res = res + val * (10 ** i)

    return int(str(res), 2)

psalm = "Praise the Lord, all you nations; extol him, all you peoples. For great is his love toward us, and the faithfulness of the Lord endures forever. Praise the Lord."

data = ''.join(format(ord(i), '08b') for i in psalm)
print(decode(data))
with open('psalm.txt', 'w') as f:
    f.write(data)

m = len(data)
r = calcRedundantBits(m)

arr = posRedundantBits(data, r)
arr = calcParityBits(arr, r)

print("Data transferred is " + arr)
print("Error Data is " + arr)
correction = detectError(arr, r)
print("The position of error is " + str(correction))

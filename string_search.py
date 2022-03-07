@profile
def brute(text, pattern):
    for i in range(0, len(text) - len(pattern) + 1):
        k = 0
        while k < len(pattern) and text[i + k] == pattern[k]:
            k += 1
        if len(pattern) == k:
            print("Pattern found at index", i, "and ending at ", i + k - 1)

@profile
def kmp(text, pattern):
    for i in range(0, len(text) - len(pattern) + 1):
        dict = kmpsub(text, pattern, i)
        if dict["pass"] is True:
            print("Pattern found at index", i, "and ending at ", i + len(pattern) - 1)
        i += dict["next"]

def kmpsub(text, pattern, index):
    m = len(pattern)
    n = len(text)
    arr = [True] * m

    for i in range(m):
        for j in range(i + 1):
            if arr[j] is True and (index + i + j >= n or text[index + i + j] != pattern[i]):
                arr[j] = False

    dict = {"pass": arr[0], "next": m}

    for i in range(1, m):
        if arr[i] is True:
            dict["next"] = i
            break

    return dict

with open('macbeth.txt') as f:
    text = f.read()
    
pattern = "break"

brute(text, pattern)
kmp(text, pattern)

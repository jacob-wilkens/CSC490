@profile
def brute(text, pattern):
    for i in range(0, len(text) - len(pattern) + 1):
        k = 0
        while k < len(pattern) and text[i + k] == pattern[k]:
            k += 1
        if len(pattern) == k:
            #print("Pattern found at index", i, "and ending at", i + k - 1)
            continue

@profile
def kmp(text, pattern):
    for i in range(0, len(text) - len(pattern) + 1):
        dict = kmpsub(text, pattern, i)
        if dict["pass"] is True:
            #print("Pattern found at index", i, "and ending at", i + len(pattern) - 1)
            continue
        i += dict["next"]

def kmpsub(text, pattern, index):
    arr = [True] * len(pattern)

    for i in range(len(pattern)):
        for j in range(i + 1):
            if arr[j] is True and (index + i + j >= len(text) or text[index + i + j] != pattern[i]):
                arr[j] = False

    dict = {"pass": arr[0], "next": len(pattern)}

    for i in range(1, m):
        if arr[i] is True:
            dict["next"] = i
            break

    return dict

class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.index = []

class Node:

    def __init__(self, key):
        self.key = key
        self.children = {}
        self.index = []

class Trie:
    root = None

    def __init__(self):
        self.root = Node(None)

    @profile
    def search(self, pattern):
        if pattern[0] in self.root.children.keys():
            return self.searchNode(self.root.children[pattern[0]], pattern)

        return None

    def searchNode(self, node, pattern):
        if len(pattern) == 1 and node.key == pattern[0]:
            return node

        if node.key == pattern[0] and pattern[1] in node.children.keys():
            return self.searchNode(node.children[pattern[1]], pattern[1:])

        return None

    def insert(self, str, index):
        currNode = self.root
        for i in range(len(str)):
            newStr = str[:i + 1]
            if i == 0:
                found = self.search(newStr)
                if found is None:
                    node = Node(newStr)
                    currNode.children[newStr] = node
                    currNode = node
                else:
                    currNode = found
            else:
                key = str[i]
                if key in currNode.children.keys():
                    currNode = currNode.children[key]
                else:
                    node = Node(key)
                    currNode.children[key] = node
                    currNode = node
        currNode.index.append(index)

    def patchInsert(self, text, patternSize):
        for i in range(len(text) - patternSize + 1):
            self.insert(text[i: i + patternSize], i)

with open('macbeth.txt') as f:
    text = f.read()
pattern = "break"

def trieSearch(text, pattern):
    myTrie = Trie()
    myTrie.patchInsert(text, len(pattern))
    for i in myTrie.search(pattern).index:
        #print("Pattern found at index", i, "and ending at", i + len(pattern) - 1)
        continue

#print("Brute Force")
brute(text, pattern)
#print("______________________")
#print("KMP")
kmp(text, pattern)
#print("______________________")
#print("TRIE")
trieSearch(text, pattern)

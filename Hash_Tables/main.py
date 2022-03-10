import re
from AddressHashTable import *
from ChainingHashTable import *

def prepareHashTable(str, htableType):
    str = (re.sub(r'[^\w\s]', '', str)).split()
    strLength = len(str)

    htable = None
    if htableType == "Chaining":
        htable = ChainingHashTable()
    else:
        htable = AddressHashTable(strLength)

    for i in range(strLength):
        htable.insert(str[i], i)

    if htableType != "Chaining":
        htable.resize()

    return htable

keyword = "death"

with open('poem.txt') as f:
    str = f.read()
    f.close()

chainhtable = addresshtbale = prepareHashTable(str, "Chaining")
chainhtable.display_hash()
print("Chaining Hash Table value for key", keyword, "is", chainhtable.search(keyword))

print("___________")

addresshtbale = prepareHashTable(str, "Address")
addresshtbale.display_hash()
print("Address Hash Table value for key", keyword, "is", addresshtbale.search(keyword))

from Item import Item
from Packing import Packing
from Bin import Bin

# 10 items: a: 2, b: 6, c: 2
a = 2 #a 5x4x3
b = 6 #b 3x3x3
c = 2 #c 6x2x2

items = [Item("a", 5, 4, 3)] * a + [Item("b", 3, 3, 3)] * b + [Item("c", 6, 2, 2)] * c
bins = []

#Implementation
for i in range(len(items)):
    newBin = Bin("Type A", 12, 9, 6)
    newBin.items.append(i)
    bins.append(newBin)

print("It took", len(bins), "bins!")
#bin_packing = Packing(items)
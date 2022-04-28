from Bin import Bin

class Packing:

    def __init__(self, items):
        self.bins = []
        self.unpacked_items = items

    def pack(self):
        pass
        
        # self.bins.append(Bin("Type A", 12, 9, 6))

        #while len(unpacked_item) != 0:
            # for items in self.unpacked_items:
                # placed = False
                # for bin in self.bins:
                    # if bin.put_item(item):
                        # bin.items.append(item)
                        # self.unpacked_items.remove(item)
                        # placed = True
                        # break
                # if not placed:
                    # newBin = Bin("Type A", 12, 9, 6)
                    # newBin.items.append(item)
                    # self.unpacked_items.remove(item)                
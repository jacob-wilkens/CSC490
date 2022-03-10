class AddressHashTable:

    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def insert(self, key, value):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] == value
                return
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value

    def hash(self, key):
        return hash(key) % self.size

    def search(self, key):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        return None

    def display_hash(self):
        print("Key:Value")
        for i in range(self.size):
            print(self.keys[i],":", self.values[i])

    def resize(self):
        self.keys = [i for i in self.keys if i]
        self.values = [i for i in self.values if i]
        self.size = len(self.keys) - 1

class ChainingHashTable:

    def __init__(self):
        self.size = 10
        self.array = [[] for _ in range(self.size)]

    def hash(self, key):
        return sum([ord(character) for character in key]) % self.size

    def insert(self, key, value):
        key_exists = False
        bucket = self.array[self.hash(key)]

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break

        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self, key):
        for i, kv in enumerate(self.array[self.hash(key)]):
            k, v = kv
            if key == k:
                return v

    # Function to display hashtable
    def display_hash(self):
        for i in range(self.size):
            print(i, end=" ")

            for j in self.array[i]:
                print("-->", end=" ")
                print(j, end=" ")

            print()

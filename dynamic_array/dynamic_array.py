class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        # insert replaces a value that is already there
        # check for free space
        if self.count == self.capacity:
            # TODO: increase size
            print("Error: Array is full")
            return

        if index >= self.count:
            # TODO: Better error handling
            print("Error: Index out of bounds")
            return

        # to insert something new at 0, we have to shift them one at a time
        # this for loop goes backwords, goes to end of array and moves right
        for i in range(self.count, index, - 1):
            self.storage[i] = self.storage[i - 1]

        self.storage[index] = value
        self.count += 1

    # append
    def append(self, value):
        # check if array is at capacity
        if self.count == self.capacity:
            # TODO: increase size
            print("Error: Array is full")
            return

        # self.count += 1
        # self.count - 1 accounts for it being zero indexed
        # self.storage[self.count - 1] = value

        # or swap them
        self.storage[self.count] = value
        self.count += 1

    def double_size(self):
        self.capacity *= 2 # make the capacity twice as big
        new_storage = [None] * self.capacity
        # need to copy the values over
        # runtime complexity is O(n)
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        # reassign the referance (change the pointer)
        self.storage = new_storage

        # old storage becomes garbage

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        # pass

    # Day 1 Assignment:
        # compute index of key
        index = self._hash_mod(key)
        # for loop, i in range length of storage
        for i in range(len(self.storage)):
            # if index of storage is None and i is index
            if self.storage[i] == None and i == index:
                # then set storage of index to key, value
                self.storage[i] = [ key,value ]
            # else if i is index (just print for now, collision handling tomorrow)
            elif i == index:
                print(f"\nWARNING: Not empty.")
                return None

    # '''
    # Notes from Lecture 2/11
    # '''
        # index = self._hash_mod(key)
        # if self.storage[index] is not None:
        #     print(f"\nWARNING:  Collision has occured at {index}")
        # else:
        #     self.storage[index] = (key, value)
        # return

    # Day 2 Assignment:
        # index = self._hash_mod(key)
        # if self.storage[index] is not None:
        # # Add a Linked List to account for collision
            
        # else:
        #     self.storage[index] = (key, value)
        # return


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        # pass

    # Day 1 Assignment:
        # compute index of key
        # index = self._hash_mod(key)
        # # if the index of storage is None
        # if self.storage[index] is None:
        #     # just print for now, collision handling tomorrow
        #     print(f"WARNING: Key not found.")
        #     return None
        # self.storage[index] = None

    # '''
    # Notes from Lecture 2/11
    # '''
        # index = self._hash_mod(key)
        # if self.storage[index] is not None:
        #     if self.storage[index][0] == key:
        #         self.storage[index] = None
        #     else:
        #         print(f"WARNING:  Collision has occured at {index}")
        # else:
        #     print(f"Warning key ({key}) not found.")
        # return

    # Day 2 Assignment:
        # index = self._hash_mod(key)
        # if self.storage[index] is not None:
        #     if self.storage[index][0] == key:
        #         self.storage[index] = None
        #     else:
        #         print(f"WARNING:  Collision has occured at {index}")
        # else:
        #     print(f"Warning key ({key}) not found.")
        # return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        # pass

    # Day 1 Assignment:
        # compute index of key
        # index = self._hash_mod(key)
        # # if storage of index is not None
        # if self.storage[index] != None:
        #     return self.storage[index]
        # else:
        #     # just print for now, collision handling tomorrow
        #     print(f"WARNING: Key doesn't match.")
        #     return None

    # '''
    # Notes from Lecture 2/11
    # '''
        # index = self._hash_mod(key)
        # if self.storage[index] is not None:
        #     if self.storage[index][0] == key:
        #         return self.storage[index][1]
        #     else:
        #         print(f"WARNING:  Collision has occured at {index}")
        # else:
        #     return None
        # return

    # Day 2 Assignment:
        index = self._hash_mod(key)
        # loop
        for i in range(self.capacity):
            index_i = self.storage[index]
            # check if index is not None and check if index[0] is the key
            if index_i is not None and index_i[0] == key:
                return index_i[1]
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        # pass

    # Day 1 Assignment:
        # Doubles the capacity of the hash table & rehash all key/value pairs.
        self.capacity *= 2
        new_storage = [None] * self.capacity
        # for index in range storage // 2
        for i in range(self.capacity // 2):
            # set node to storage index
            node = self.storage[i]
            # if node is not None, pass for now, collision handling tomorrow
            if node != None:
                pass
        # reassign the referance (change the pointer)
        self.storage = new_storage

    # '''
    # Notes from Lecture 2/11
    # '''
        # old_storage = self.storage
        # self.capacity *= 2
        # self.storage = [None] * self.capacity

        # for item in old_storage:
        #     self.insert(item[0], item[1])

    # Day 2 Assignment:
        # old_storage = self.storage
        # self.capacity *= 2
        # self.storage = [None] * self.capacity

        # for item in old_storage:
        #     self.insert(item[0], item[1])



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

# '''
# Notes from Lecture 2/11
# '''
    # ht1.insert("key1", "hello")
    # ht1.insert("unicorn", "goodbye")
    # ht1.remove("key1")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
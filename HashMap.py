__author__ = 'RonakSumbaly'

'''
    KPCB Engineering Fellows Application

    PURPOSE:
    A fixed-size hash map that associates string keys
    with arbitrary data object references.

    HASHING FUNCTION:
    The implementation uses Python's native hash() function [1]
    [1]: https://docs.python.org/2/library/functions.html#hash

    INTERPRETATION:
    The fixed size hash map was created using a list of tuples. Each entry's
    key is hashed and stored at that location of the list.

    COLLISION RESOLUTION:
    In this implementation, Linear Probing [2] is used for collision resolution.
    If two different keys have the same hash value, the new entry will be
    placed at the next free hash value location. If an entry with an already
    existing key is inputted, the value for that key will be replaced with the
    new entry value.
    [2]: https://en.wikipedia.org/wiki/Linear_probing

    COMPLEXITY:
    If the key entries are evenly distributed across the array, the performance for
    set(), get() and delete() will be O(1). In case of collision the next free hash
    value location is found which would make the worst-case complexity O(N).
'''


class HashMap(object):
    def __init__(self, size):
        """

        :param size: number of objects for hash map
        :return: an instance of the class with pre-allocated space
                 for the give number of objects

        """

        self.name = "HashMap Function"
        self.description = "Using primitive types, implement a fixed size hash map -" \
                           "Associates string keys with arbitrary data object references."
        self.size = size  # size of the hash map
        self.hashMap = [(None, None)] * self.size
        self.valueCount = 0  # values contained in the hash map

    def set(self, key, value):
        """

        :param key: key entry for hash map
        :param value: value entry for hash map
        :return: stores the given key/value pair in the hash map.
                 a boolean value indicating success / failure of the operation.

        """

        pos = self.getNextOpenHashPosition(key)

        if pos is not None:
            self.hashMap[pos] = (key, value)
            self.valueCount += 1
            return True
        else:
            return False

    def get(self, key):
        """

        :param key: key/value entry to retrieve from hash map
        :return: return the value associated with the given key, or null if no value is set.

        """

        pos = self.getNextOpenHashPosition(key)  # get position of string

        if self.hashMap[pos][0] == key:
            return self.hashMap[pos][1]
        else:
            return self.search(pos, key)[1]

    def delete(self, key):
        """

        :param key: key entry to delete in the hash map
        :return: delete the value associated with the given key, returning the value on success or null if the key has no value

        """

        pos = hash(key) % self.size

        if self.hashMap[pos][0] == key:
            self.hashMap[pos] = (None, None)
            self.valueCount -= 1
        else:
            (pos, value) = self.search(pos, key)
            if value is not None:
                self.hashMap[pos] = (None, None)
                self.valueCount -= 1

    def load(self):
        """

        :return: a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure.
                 since the size of the dat structure is fixed, this should never be greater than 1.

        """
        return (self.valueCount) / float(self.size)

    def getNextOpenHashPosition(self, key):
        """

        :param key: key entry of hash map
        :return: locates and returns the next free hash value location in the hash map

        """

        pos = hash(key) % self.size

        if self.hashMap[pos][0] is None:
            return pos

        else:
            nextPos = (pos + 1) % self.size

            while self.hashMap[nextPos][0] is not None and self.hashMap[nextPos][0] != key \
                    and nextPos != pos:
                nextPos = (nextPos + 1) % self.size

            if self.hashMap[nextPos][0] is None or self.hashMap[nextPos][0] == key:
                return nextPos

            else:
                return None

    def search(self, pos, key):
        """

        :param pos: current position in the hash map
        :param key: key/value entry to retrieve from hash map
        :return: searches hash map for the value corresponding to the input key,
                 returns the value if successful else null is returned.

        """

        nextPos = (pos + 1) % self.size

        while self.hashMap[nextPos][0] != key and nextPos != pos:
            nextPos = (nextPos + 1) % self.size

        if self.hashMap[nextPos][0] == key:
            return (nextPos, self.hashMap[nextPos][1])
        else:
            return (None, None)

    def printHashMap(self):
        """

        :return: hash map with all key/value pairs

        """
        return self.hashMap

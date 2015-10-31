__author__ = 'RonakSumbaly'

from HashMap import HashMap

class HashMapTest(HashMap):

    if __name__ == "__main__":

        map = HashMap(10)
        # create hash map with following key / value pairs
        map.set(1 , 'a')
        map.set(2 , 'b')
        map.set(3 , 'c')
        map.set(4 , 'd')
        map.set(5 , 'e')
        map.set(6 , 'f')
        map.set(7 , 'g')
        map.set(8 , 'h')
        map.set(9 , 'i')
        map.set(11, 'j') # linear probing applied since hash value is same with (1,'a')

        # print the entire hash map
        print "HASH MAP: "
        print map.printHashMap()

        # assertions to test if value stored are correct
        assert map.get(1) == 'a'
        assert map.get(2) == 'b'
        assert map.get(3) == 'c'
        assert map.get(4) == 'd'
        assert map.get(5) == 'e'
        assert map.get(6) == 'f'
        assert map.get(7) == 'g'
        assert map.get(8) == 'h'
        assert map.get(9) == 'i'
        assert map.get(11) == 'j'

        # add new key/value into hash map but since hash map is full a False is returned
        assert map.set(10, 'first') == False

        # delete key = 11 from hash map
        map.delete(11)

        # since map is not full anymore the key/value pair is added
        assert map.set(10, 'first') == True

        # print the load value for the hash map - since full the value is 1.0
        print "LOAD VALUE: ",
        print map.load() # load value

        # delete key = 10 , 7 from hash map
        map.delete(10)
        map.delete(7)

        print "\nHASH MAP: "
        print map.printHashMap()
        # print the load value for the hash map - since one pair is deleted the value is 0.9
        print "LOAD VALUE: ",
        print map.load() # same load value

        print "ALL TEST CASES PASSED."

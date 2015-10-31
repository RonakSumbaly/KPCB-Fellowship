2016 KPCB Fellowship Challenge Problem
--------------------------------------

Details
-------
Implementation Language - Python 2.7

How to run the program
-----------------------
To run the program, the system will require Python to be installed on it. Run the following command for testing the script:
python HashMapTest.py

Output
------
The results of the unit tests will be displayed, which are used to test the set(), get(), delete() and load().

Hashing Function
----------------
The implementation uses Python's native hash() function [1]
[1]: https://docs.python.org/2/library/functions.html#hash

Implementation
--------------
The fixed size hash map was created using a list of tuples. Each entry's 
key is hashed and stored at that location of the list.

Collision Resolution
--------------------
In this implementation, Linear Probing [2] is used for collision resolution.
If two different keys have the same hash value, the new entry will be
placed at the next free hash value location. If an entry with an already
existing key is inputted, the value for that key will be replaced with the new entry value.
[2]: https://en.wikipedia.org/wiki/Linear_probing

Algorithm Complexity
--------------------
Without collision : set, get, delete - O(1)
With collision : Worse Case - set, get, delete  - O(N)
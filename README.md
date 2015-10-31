# 2016 KPCB Fellowship Challenge Problem

Using only primitive types, implement a **fixed-size hash map** that associates string keys
with arbitrary data object references (you don't need to copy the object). 

Your data structure should be optimized for algorithmic runtime and memory usage. 
You should not import any external libraries, and may not use primitive hash map or dictionary types in languages like Python or Ruby.

## Details

*Implementation Language* - Python 2.7

## How to run the program

To run the program, the system will require Python to be installed on it. Run the following command for testing the script
`python HashMapTest.py`

## Output

The results of the unit tests will be displayed, which are used to test the set(), get(), delete() and load().

## Hashing Function

The implementation uses Python's native [hash() function](https://docs.python.org/2/library/functions.html#hash)

## Implementation

The fixed size hash map was created using a list of tuples. Each entry's 
key is hashed and stored at that location of the list.

## Collision Resolution

In this implementation, [Linear Probing](https://en.wikipedia.org/wiki/Linear_probing) is used for collision resolution.
If two different keys have the same hash value, the new entry will be
placed at the next free hash value location. If an entry with an already
existing key is inputted, the value for that key will be replaced with the new entry value.

## Algorithm Complexity

* ##### Without collision
	* Best/Average/Worse Case - set, get, delete - O(1)
* ##### With collision
	* Worse Case - set, get, delete  - O(N)
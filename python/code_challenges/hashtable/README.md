 # Hashtables
a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.
## Challenge
Hashing is a way  used to uniquely identify a specific object from a group of similar objects and convert strings to ascii code and then put each value in its index and if collision happens use linked list to put multi nodes.

## Approach & Efficiency
The Efficiency of the Big O time is O(n)

The Efficiency of the Big O space is O(1)

## API

### hash
Arguments: key
Returns: Index in the collection for that key
### get
Arguments: key
Returns: Value associated with that key in the table
### add
Arguments: key, value
Returns: nothing
This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
### contains
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.

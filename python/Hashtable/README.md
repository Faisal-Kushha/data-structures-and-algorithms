# Hashtables

It is a data structure that maps keys to values. It is one part of a technique called hashing, the other of which is a hash function. A hash function is an algorithm that produces an index of where a value can be found or stored in the hash table.

## Challenge

Hashtables Implementation

## Approach & Efficiency

Hash maps take advantage of an array’s O(1) read access. Instead of adding elements to an array from beginning to end, a hash map uses a “hash function” to place each item at a precise index location, based off it’s key.
Big O: O(1)

## API

-   [x] add

Arguments: key, value

Returns: nothing

This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

-   [x] get

Arguments: key

Returns: Value associated with that key in the table

-   [x] contains

Arguments: key

Returns: Boolean, indicating if the key exists in the table already.

-   [x] hash

Arguments: key

Returns: Index in the collection for that key

Structure and Testing

-   [x] Adding a key/value to your hashtable results in the value being in the data structure
-   [x] Retrieving based on a key returns the value stored
-   [x] Successfully returns null for a key that does not exist in the hashtable
-   [x] Successfully handle a collision within the hashtable
-   [x] Successfully retrieve a value from a bucket within the hashtable that has a collision
-   [x] Successfully hash a key to an in-range value

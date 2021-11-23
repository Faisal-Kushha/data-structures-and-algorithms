# Challenge Summary

-   Write a function that LEFT JOINs two hashmaps into a single data structure.

-   Write a function called left join

-[x] Arguments: two hash maps

-   The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.

-   The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.

-[x] Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Whiteboard Process

![Code33](Code33.png)

## Approach & Efficiency

Create a function that take 2 hashmaps as input, then declare an empty array and check if the hashmap is empty. Loop through the first hashmap, then declare a second empty array and append the key for the first hash then append the value for the first hash after that append the value for the second hash. finally let the first array append the second array and return it.

Big O: O(n^2), O(n)

## Solution

```
def left_join(hashmap1, hashmap2):
    arr1 = []
    if hashmap1.buckets == hashmap1.size*[None] or hashmap2.buckets == hashmap2.size*[None]:
        return 'Hash table is empty'
    for item in hashmap1.buckets:
        if item:
            arr2 = []
            arr2.append(item.head.value[0])
            arr2.append(hashmap1.get(item.head.value[0]))
            arr2.append(hashmap2.get(item.head.value[0]))
            arr1.append(arr2)
    return arr1

```

## Pull Request

https://github.com/Faisal-Kushha/data-structures-and-algorithms/pull/42

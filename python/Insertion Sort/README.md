# Code Challenge: Class 26

## Challenge Summary

Write an Insertion sort function that takes an array and return it sorted.

[BLOG](python/Insertion Sort/BLOG.md)

## Whiteboard Process

![code26](python/Insertion Sort/Code26.png)

## Approach & Efficiency

1. Create a function that takes an array of numbers as an argument
2. A for loop in range (1,len(arr))
3. A while loop let j = i-1 and temp = arr[i]
4. Decleare another loop while j more than or equal zero and temp less than arr[j]
5. If true arr[j+1] = arr[j] and j = j-1
6. After the while loop break let arr[j+1] = temp
7. After the for loop break return the array

BigO: O(n^2), O(1)

## Solution

```
def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = temp
    return arr
```

## Pull Request

https://github.com/Faisal-Kushha/data-structures-and-algorithms/pull/36

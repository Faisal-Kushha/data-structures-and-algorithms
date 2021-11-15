# Code Challenge: Class 26

## Challenge Summary

Write a function that takes an array as an argument then find the mid point by slicing it and return a sorted array

## Approach & Efficiency

[BLOG](BLOG.md)
BigO: O(n \* log n), O(n)

## Solution

```
def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)
    return arr


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
```

## Implementation

-   [x] Provide a visual step through for each of the sample arrays based on the provided pseudo code
-   [x] Convert the pseudo-code into working code in your language
-   [x] Present a complete set of working tests

## Requirements

-   [x] Write unit tests
-   [x] Follow the template for a well-formatted README
-   [x] Submit the assignment depend on instructions

## Test Requirements

-   [x] Test The method by these samples:
    -   [x] Reverse-sorted: [20, 18, 12, 8, 5, -2]
    -   [x] Few uniques: [5, 12, 7, 5, 5, 7]
    -   [x] Nearly-sorted: [2, 3, 5, 7, 13, 11]

## Developer

Faisal Kushha

I worked in collaboration with Jehad Abu Awwad

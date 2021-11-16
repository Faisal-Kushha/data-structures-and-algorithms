# Code Challenge: Class 28

## Challenge Summary

Write a function that takes three argument (array, the first index, the last index) then sort the array in ascending way

## Approach & Efficiency

[BLOG](BLOG.md)
BigO: O(n), O(n \* log(n))

## Solution

```
def QuickSort(arr, left, right):

    if left < right:
        position = partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)
    return arr


def partition(arr, left, right):

    pivot = arr[right]
    low = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            Swap(arr, i, low)
    Swap(arr, right, low + 1)
    return low + 1


def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

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

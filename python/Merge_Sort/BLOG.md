```
i j k arr
1 1 2 [4, 23]
1 2 3 [4, 8, 23]
1 1 2 [15, 16]
1 2 3 [15, 16, 42]
3 3 6 [4, 8, 15, 16, 23, 42]
[4, 8, 15, 16, 23, 42]

```

The merge sort methods takes the array as an argument and slice it at the mid point for two parts that return the left right and the array that will be used in the merge method which initialize a three counters from zero and start comparing the first element in the left slice and the first element in the right slice if it's less than it. It will modify the array to be the lower value increasing it's own counter and after all loops finish it will set the remaining entries in the array to right, additionally set the remaining entries in the array to left.

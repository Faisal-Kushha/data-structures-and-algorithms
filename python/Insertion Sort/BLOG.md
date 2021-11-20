```
Array i j temp
[8,4,23,42,16,15] 1 0 4
[4,8,23,42,16,15] 2 1 23
[4,8,23,42,16,15] 3 2 42
[4,8,23,42,16,15] 4 3 16
[4,8,16,23,42,15] 5 4 15
[4,8,15,16,23,42]
```

Insertion sort function will take the array as an argument and loop through it, it will start by the first by defining a counter and go through the array elements one by one move elements of arr[0..i-1] and save it as a temporery variable, and it will keep looping and do the same proccess till it sort all of the elements of the array.

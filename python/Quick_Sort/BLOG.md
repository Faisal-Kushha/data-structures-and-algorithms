```
arr, left, right
[8, 4, 15, 42, 16, 23], 0, 5
[4, 8, 15, 42, 16, 23], 0, 1
[4, 8, 15, 16, 23, 42], 3, 5
```

Quick sort handles sorting an array with left and right points which is the first and the last element of the array. If the left is less than the right we divide the array by defining the low value which is less than left by one. After that we loop through the array from the left to the right ==> if the value of the array is less than the pivot which is the last element in the array, after that the low will be increased by one. After that we will swap the element by the lowest value. Then another swap will take the array and the right value with the low increased by one returning the low value increased by one.

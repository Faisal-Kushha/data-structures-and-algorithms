import math
def binary_search(array, number):
    lowest = 0
    highest = len(array)-1
    while lowest <= highest:
        if(number in array):
            middle= math.floor((lowest + highest) / 2)
            if array[middle] < number:
                lowest = middle + 1
            elif array[middle] > number:
                highest = middle - 1
            else:
                return middle
        else:
            return -1
if __name__=="__main__":
    print(binary_search([1, 2, 3, 4, 5,6], 8))

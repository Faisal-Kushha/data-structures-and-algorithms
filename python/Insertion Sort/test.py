from insertion_sort import insertion_sort


def test_reverse_sorted():
    arr = [20, 18, 12, 8, 5, -2]
    insertion_sort(arr)
    assert arr[0] == -2
    assert arr[1] == 5
    assert arr[-1] == 20


def test_few_uniques():
    arr = [5, 12, 7, 5, 5, 7]
    insertion_sort(arr)
    assert arr[0] == 5
    assert arr[1] == 5
    assert arr[-1] == 12


def test_nearly_sorted():
    arr = [2, 3, 5, 7, 13, 11]
    insertion_sort(arr)
    assert arr[0] == 2
    assert arr[1] == 3
    assert arr[-1] == 13

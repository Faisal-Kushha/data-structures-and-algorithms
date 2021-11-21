from hashtable import HashTable, repeated_word

"""
"a"
ord("d") = 100
100 * 7 = 700
700 % 1024 = 700

-----------------
"dd"
200
200 * 7 = 1400
1400 % 1024 = 376
"""


def test_hash():
    hashtable = HashTable()
    expected = 700
    actual = hashtable._HashTable__hash("d")
    assert actual == expected


def test_hash_word():
    hashtable = HashTable()
    expected = 376
    actual = hashtable._HashTable__hash("dd")
    assert actual == expected


def test_add():
    hashtable = HashTable()
    hashtable.add('F', 70)
    actual = 70
    expected = hashtable.get('F')
    assert actual == expected


def test_get():
    hashtable = HashTable()
    hashtable.add('FF', 140)
    actual = 140
    expected = hashtable.get('FF')
    assert actual == expected


def test_get_incorrect_key():
    hashtable = HashTable()
    actual = hashtable.get('A')
    expected = None
    assert actual == expected


def test_collision_hashtable():
    hashtable = HashTable()
    hashtable.add('FF', 140)
    actual = hashtable.contains('FF')
    expected = True
    assert actual == expected


def test_collision_value():
    hashtable = HashTable()
    hashtable.add('FF', 140)
    actual = hashtable.get('FF')
    expected = 140
    assert actual == expected


def test_happy_path():
    text = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(text)
    excepted = 'a'
    assert actual == excepted


def test_edge_case():
    text = ''
    actual = repeated_word(text)
    excepted = 'No text'
    assert actual == excepted


def test_expected_failure():
    text = "Once upon a time, there was very brave princess who..."
    actual = repeated_word(text)
    excepted = "No repeated word"
    assert actual == excepted

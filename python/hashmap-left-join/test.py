import pytest
from hashmap_left_join import *


def test_happy_path(prepared_hash1, prepared_hash2):
    actual = left_join(prepared_hash1, prepared_hash2)
    expected = [['outfit', 'garb', None], ['guide', 'usher', 'follow'], [
        'wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse']]
    assert actual == expected


def test_edge_case():
    hashtable_one = HashTable()
    hashtable_two = HashTable()

    actual = left_join(hashtable_one, hashtable_two)
    expected = 'Hash table is empty'
    assert actual == expected


def test_expected_failure(prepared_hash1):
    hashtable_two = HashTable()
    hashtable_two.add('hi', 'averse')
    hashtable_two.add('wrath', 'delight')
    hashtable_two.add('diligent', 'idle')
    hashtable_two.add('guide', 'follow')
    hashtable_two.add('flow', 'jam')
    actual = left_join(prepared_hash1, hashtable_two)
    expected = [['wrath', 'anger', 'delight'], ['outfit', 'garb', None], [
        'diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]
    assert actual != expected


@pytest.fixture
def prepared_hash1():
    hashtable_one = HashTable()
    hashtable_one.add('fond', 'enamored')
    hashtable_one.add('wrath', 'anger')
    hashtable_one.add('diligent', 'employed')
    hashtable_one.add('outfit', 'garb')
    hashtable_one.add('guide', 'usher')
    return hashtable_one


@pytest.fixture
def prepared_hash2():
    hashtable_two = HashTable()
    hashtable_two.add('fond', 'averse')
    hashtable_two.add('wrath', 'delight')
    hashtable_two.add('diligent', 'idle')
    hashtable_two.add('guide', 'follow')
    hashtable_two.add('flow', 'jam')
    return hashtable_two

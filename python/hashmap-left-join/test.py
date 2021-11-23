import pytest
from hashmap_left_join import *


def test_happy_path(prepared_hash1, prepared_hash2):
    actual = left_join(prepared_hash1, prepared_hash2)
    expected = [['outfit', 'garb', None], ['guide', 'usher', 'follow'], [
        'wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse']]
    assert actual == expected


def test_edge_case():
    hashmap1 = HashTable()
    hashmap2 = HashTable()

    actual = left_join(hashmap1, hashmap2)
    expected = 'Hash table is empty'
    assert actual == expected


def test_expected_failure(prepared_hash1):
    hashmap2 = HashTable()
    hashmap2.add('hi', 'averse')
    hashmap2.add('wrath', 'delight')
    hashmap2.add('diligent', 'idle')
    hashmap2.add('guide', 'follow')
    hashmap2.add('flow', 'jam')
    actual = left_join(prepared_hash1, hashmap2)
    expected = [['wrath', 'anger', 'delight'], ['outfit', 'garb', None], [
        'diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]
    assert actual != expected


@pytest.fixture
def prepared_hash1():
    hashmap1 = HashTable()
    hashmap1.add('fond', 'enamored')
    hashmap1.add('wrath', 'anger')
    hashmap1.add('diligent', 'employed')
    hashmap1.add('outfit', 'garb')
    hashmap1.add('guide', 'usher')
    return hashmap1


@pytest.fixture
def prepared_hash2():
    hashmap2 = HashTable()
    hashmap2.add('fond', 'averse')
    hashmap2.add('wrath', 'delight')
    hashmap2.add('diligent', 'idle')
    hashmap2.add('guide', 'follow')
    hashmap2.add('flow', 'jam')
    return hashmap2

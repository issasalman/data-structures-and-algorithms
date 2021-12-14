from hashtable import __version__
from hashtable.hashtable import HashTable
from hashtable.hashmap_left_join import left_join



import pytest

def test_left_right(left_hash, right_hash ):
    assert left_join(left_hash, right_hash) == [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['delight', 'employed', 'idle'], ['outifit', 'garp', 'None'], ['guide', 'usher', 'follow']]

def test_left_emptyright(left_hash, empty_hash ):
    assert left_join(left_hash, empty_hash) == [['fond', 'enamored', 'None'], ['wrath', 'anger', 'None'], ['delight', 'employed', 'None'], ['outifit', 'garp', 'None'], ['guide', 'usher', 'None']]

def test_emptyleft_right(empty_hash, right_hash ):
    assert left_join(empty_hash, right_hash) == []

@pytest.fixture
def left_hash():
    left_hash = HashTable()
    left_hash.add('fond', 'enamored')
    left_hash.add('wrath', 'anger')
    left_hash.add('delight', 'employed')
    left_hash.add('outifit', 'garp')
    left_hash.add('guide', 'usher')
    return left_hash

@pytest.fixture
def right_hash():
    right_hash = HashTable()
    right_hash.add('fond', 'averse')
    right_hash.add('wrath', 'delight')
    right_hash.add('delight', 'idle')
    right_hash.add('guide', 'follow')
    right_hash.add('flow', 'jam')
    return right_hash

@pytest.fixture
def empty_hash():
    empty_hash = HashTable()
    return empty_hash

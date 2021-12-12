from hashtable import __version__
from hashtable.linked_list import LinkedList
from hashtable.hashtable import HashTable


def test_version():
    assert __version__ == '0.1.0'


def test_add():
    hashtable = HashTable()
    actual=hashtable.add('ahmad', 30)
    expected=['ahmad', 30]
    assert expected==actual

def test_get():
    hashtable = HashTable()
    hashtable.add('ahmad', 30)
    actual=hashtable.get("ahmad")
    expected=30
    assert expected==actual

def test_contain():
    hashtable = HashTable()
    hashtable.add('ahmad', 30)
    actual=hashtable.contains("ahmad")
    expected=True
    assert expected==actual


def test_get_None():
    hashtable = HashTable()
    hashtable.add('ahmad', 30)
    actual=hashtable.get("issa")
    expected=None
    assert expected==actual


def test_contain_None():
    hashtable = HashTable()
    hashtable.add('ahmad', 30)
    actual=hashtable.contains("issa")
    expected=None
    assert expected==actual



def test_get_collision():
    hashtable = HashTable()
    hashtable.add('ahmad', 30)
    hashtable.add('hamad', 35)
    assert hashtable.get("ahmad")==30



def test_contain_collision():
    hashtable = HashTable()
    hashtable.add('ahmad', 30)
    hashtable.add('hamad', 35)
    assert hashtable.contains("ahmad")==True


def test_hash_size():
      hashtable = HashTable()
      assert 0 <= hashtable.hash("Issa") <= 1024







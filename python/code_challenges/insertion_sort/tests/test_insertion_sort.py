from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort


def test_version():
    assert __version__ == '0.1.0'

def test_empty_array():


    expected ="empty array"
    actual=insertion_sort([])
    assert expected==actual

def test_normal_array():

    expected =[4, 8, 15, 16, 23, 42]
    actual=insertion_sort([8,4,23,42,16,15])
    assert expected==actual

def test_Reverse_sorted_array():
    expected =[-2, 5, 8, 12, 18, 20]
    actual=insertion_sort([20,18,12,8,5,-2])
    assert expected==actual


def test_Few_uniques_sorted_array():
    expected =[5, 5, 5, 7, 7, 12]
    actual=insertion_sort([5,12,7,5,5,7])
    assert expected==actual


def test_Nearly_sorted_array():
    expected =[2, 3, 5, 7, 11, 13]
    actual=insertion_sort([2,3,5,7,13,11])
    assert expected==actual






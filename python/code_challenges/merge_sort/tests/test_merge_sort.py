from merge_sort import __version__
from merge_sort.merge_sort import merge_sort


def test_version():
    assert __version__ == '0.1.0'


def test_merge_sort():
    expected =[1, 2, 5, 7, 9, 12]
    actual=merge_sort([12, 1, 9, 5, 2, 7])
    assert expected==actual


def test_merge_reversed_sort():
    expected =[-2, 5, 8, 12, 18, 20]
    actual=merge_sort([20,18,12,8,5,-2])
    assert expected==actual

def test_merge_Few_uniques_sort():
    expected =[5, 5, 5, 7, 7, 12]
    actual=merge_sort([5,12,7,5,5,7])
    assert expected==actual

def test_merge_Nearly_sorted():
    expected =[2, 3, 5, 7, 11, 13]
    actual=merge_sort([2,3,5,7,13,11])
    assert expected==actual

def test_merge_empty_array():
    expected ="empty array"
    actual=merge_sort([])
    assert expected==actual

def test_merge_one_number_array():
    expected =[1]
    actual=merge_sort([1])
    assert expected==actual




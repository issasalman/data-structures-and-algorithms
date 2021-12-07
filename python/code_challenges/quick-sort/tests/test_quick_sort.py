from quick_sort import __version__
from quick_sort.quick_sort import quick_sort


def test_version():
    assert __version__ == '0.1.0'


def test_quick_sort():
    expected =[1, 2, 5, 7, 9, 12]
    arr=[12, 1, 9, 5, 2, 7]
    actual=quick_sort(arr,0,(len(arr)-1))
    assert expected==actual


def test_quick_reversed_sort():
    expected =[-2, 5, 8, 12, 18, 20]
    arr=[20,18,12,8,5,-2]
    actual=quick_sort(arr,0,(len(arr)-1))
    assert expected==actual

def test_quick_Few_uniques_sort():
    expected =[5, 5, 5, 7, 7, 12]
    arr=[5,12,7,5,5,7]
    actual=quick_sort(arr,0,(len(arr)-1))
    assert expected==actual

def test_quick_Nearly_sorted():
    expected =[2, 3, 5, 7, 11, 13]
    arr=[2,3,5,7,13,11]
    actual=quick_sort(arr,0,(len(arr)-1))
    assert expected==actual

def test_quick_empty_array():
    expected ="empty array"
    arr=[]
    actual=quick_sort(arr,0,(len(arr)-1))
    assert expected==actual

def test_quick_one_number_array():
    expected =[1]
    arr=[1]
    actual=quick_sort(arr,0,(len(arr)-1))
    assert expected==actual

def quick_sort(arr, left, right):
    if len(arr)==0:
        return "empty array"
    elif len(arr)==1:
        return arr
    print("left",left)
    print("right",right)
    # print("arr",arr)
    print("")

    if left < right:
        print("hi")
        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)

        return arr


def partition(arr, left, right):
    print("leftp",left)
    print("rightp",right)
    # print("arrp",arr)

    print("")
    pivot = arr[right]
    low = left
    print("lowp",low)

    for i in range(left, right):
        if arr[i] <= pivot:

            Swap(arr, i, low)
            low += 1
            print("it will not swap")

    print("")
    # print("arrs",arr)
    print("rights",right)
    print("lows",low)
    print("")

    Swap(arr, right, low)
    return low

def Swap(arr, i, low):

    print("swaping")
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
    print("arrs",arr)


a=[12, 1, 9, 5, 2, 13]
print(quick_sort(a,0,(len(a)-1)))


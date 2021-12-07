def merge_sort(arr):

    n =len(arr)
    if n==0:
        return "empty array"
    elif n==1:
        return arr

    if n > 1:

        mid = n//2

        left = arr[0:mid]

        right = arr[mid:n]
        print("")
        print("left",left)
        print("right",right)
        print("arr",arr)
        print("")

        merge_sort(left)
        merge_sort(right)
        print("")

        print("left1",left)
        print("right1",right)
        print("arr1",arr)
        print("")

        return  merge(left,right,arr)

def merge(left,right,merging_arr):
    i,j,k =0,0,0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merging_arr[k] = left[i]
            i += 1
        else:
            merging_arr[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j <len(right):
            merging_arr[k] = right[j]
            j +=1
            k += 1
    elif j == len(right):
        while i <len(left):
            merging_arr[k] = left[i]
            i +=1
            k += 1
    print("sort",merging_arr)
    return merging_arr


if __name__ == '__main__':
    arr1 = [12, 1, 9, 5, 2, 7]
    arr2=[20,18,12,8,5,-2]
    arr3=[5,12,7,5,5,7]
    arr4=[2,3,5,7,13,11]
    print(merge_sort(arr1))


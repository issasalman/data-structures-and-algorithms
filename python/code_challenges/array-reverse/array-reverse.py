arr1 = list(input())


def reverseArray():
    """
    This function is to reverse any elements
    """
    i = 0

    j = len(arr1)-1

    while i < j:
        arr1[i], arr1[j] = arr1[j], arr1[i]
        i += 1
        j -= 1

        print(arr1)
        return arr1


if __name__ == "__main__":
    reverseArray()

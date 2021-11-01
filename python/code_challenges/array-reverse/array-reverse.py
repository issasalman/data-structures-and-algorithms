

def reverseArray(arr1):
    """
    This function is to reverse any elements
    """


    if len(arr1)<=1:
        print (arr1)
        return arr1
    else:
        i = 0

        j = len(arr1)-1

        while i <= j:

          item=arr1[i]
          arr1[i]=arr1[j]
          arr1[j]=item

          i += 1
          j -= 1

          print(arr1)
          return arr1



print(reverseArray([5,1,4,7,8,9]))

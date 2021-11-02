def binary(array,number):

  end=len(array)-1
  start=0
  middle=0
  while start<=end :
      middle=(start+end)//2

      if array[middle]<number:
       start=middle+1
      elif array[middle] > number:
        end=middle-1

      else:
        return middle
  return -1


print(binary([1,5,74,7,7],74))

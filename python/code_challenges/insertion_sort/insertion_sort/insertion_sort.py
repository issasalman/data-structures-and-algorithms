def insertion_sort(arr=[]):
  if len(arr)==0:
      return "empty array"

  for i in range(1,len(arr)):

    j=i-1
    temp=arr[i]
    print ("i" ,arr[i])
    print("j",arr[j])
    print ("temp",temp)

    print("======")

    while j>=0 and temp < arr[j]:
      print("Hi")

      arr[j+1]=arr[j]
      j=j-1
      


    arr[j+1]=temp
    print(arr)

  return(arr)

print(insertion_sort([8,4,23,42,16,15]))
# print(insertion_sort([20,18,12,8,5,-2]))
# print(insertion_sort([5,12,7,5,5,7]))
# print(insertion_sort([2,3,5,7,13,11]))
# print(insertion_sort([]))





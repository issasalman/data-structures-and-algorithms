def insertShiftArray(arr,n):
    arrayLength=0

    for i in arr:
        arrayLength+=1
    middleIndex=int(arrayLength/2)
    arr1=[None]*(arrayLength+1)
    arr1[middleIndex]=n
    for index,i in enumerate(arr):

        if arr1[index]==None:
           arr1[index]=(i)
           index+=1
        else :
            arr1[index+1]=(i)


    arr=arr1
    return arr


print(insertShiftArray([1,5,4,7,7,8,4,7,8,5],100))


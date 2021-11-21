names=["A","B","C","D","E"]
def DuckDuckGoose(names,k):
    position = k-1
    index =0
    list_len=len(names)
    while list_len>1 :
        index=(position+index)% list_len
        (names.pop(index))
        list_len -=1

    return names
if __name__=="__main__":
    x=DuckDuckGoose(names,3)
    print(x)

def InsertionSort(numbers):
    for i in range(len(numbers)):
        index=numbers[i]
        j=i
        while j>0 and numbers[j-1]>index:
            numbers[j]=numbers[j-1]
            j=j-1
        numbers[j]=index

if __name__=="__main__":
    l=[1,11,2,0,21,-9]
    InsertionSort(l)
    print l
    

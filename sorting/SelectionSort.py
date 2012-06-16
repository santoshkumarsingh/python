'''his type of sorting is called "Selection Sort" because it works by
repeatedly element. It works as follows: first find the smallest in
the array and exchange it with the element in the first position,
then find the second smallest element and exchange it with the element
in the second position, and continue in this way until the entire array
is sorted.'''

def SelectionSort(numbers):
    size=len(numbers)
    for i in range(size):
        
        min=i
        for j in range(i+1,size):
            if numbers[j]< numbers[min]:
                min=j
        temp=numbers[i]
        numbers[i]=numbers[min]
        numbers[min]=temp

if __name__=="__main__":
    l=[1,11,2,0,21,-9]
    SelectionSort(l)
    print l
    
    

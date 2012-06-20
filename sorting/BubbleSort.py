'''Bubble Sort is an elementary sorting algorithm.'''
'''It works by repeatedly exchanging adjacent elements, '''
'''if necessary. When no exchanges are required, the file is sorted.'''
def BubbleSort(array):
    for x in range(len(array)-1,-1,-1):
        
        for y in range(1,x+1):
            if array[y-1]>array[y]:
                temp=array[y-1]
                array[y-1]=array[y]
                array[y]=temp
            
if __name__=="__main__":
    l=[1,11,2,0,21,-9]
    BubbleSort(l)
    print l
    

def MergeSort(left, right, lt):
    """Assumes left and right are sorted lists.lt defines an ordering on the elements of the lists.Returns a new sorted(by lt) list containing the same elementsas (left + right) would contain."""
    result = []
    
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if lt(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def Sort(L, lt = lambda x,y: x < y):
    """Returns a new sorted list containing the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = Sort(L[:middle], lt)
        right = Sort(L[middle:], lt)
        print left, right
    return MergeSort(left, right, lt)
if __name__=="__main__":
    
    L = [35, 4, 5, 29, 17, 58, 0]
    newL = Sort(L)
    print 'Sorted list =', newL

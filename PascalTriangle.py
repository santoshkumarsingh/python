'''This is simple implementation of pascal triangle in python'''
def pascal(n):
    if n == 1:
        return [ [1] ]
    else:
        result = pascal(n-1)
        lastRow = result[-1]
        result.append( [ (a+b) for a,b in zip([0]+lastRow, lastRow+[0]) ] )
        return result


if __name__=="__main__":
    h = int(raw_input("Please enter the height of the triangle: "))
    for i in pascal(h):
        print " " * (h * 2), i
        h -= 1

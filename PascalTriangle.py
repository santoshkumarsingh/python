'''This is simple implementation of pascal triangle in python'''
level = 0
def trace(f):
    def g(*args):
        global level
        indent = '|   ' * level + '|-- '

        argstr = ", ".join([repr(a) for a in args])
        print indent + f.__name__ + argstr

        level += 1
        value = f(*args)
        level -= 1

        print indent + ' return ' + repr(value)
        return value
    return g




@trace
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
    print 
    for i in pascal(h):
        print " " * (h * 2), i
        h -= 1

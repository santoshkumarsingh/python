'''Factorial of a number using recursion'''
def fact(number):
    '''base case'''
    if number==0 or number==1:
        return 1
    else:
        return number*fact(number-1)


if __name__=="__main__":
    print fact(4)


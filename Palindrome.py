#WITHOUT RECURSION
def isPalindrome(value):
    '''This program introduces the IsPalindrome boolean method'''
    '''A palindrome has the same letters on both ends of the string'''
    ''' This means "civic" is a palindrome, but "perls" is not.'''
    min=0
    max=len(value)-1
    while True:
        if min>max:
            return True
        a=value[min]
        b=value[max]
        if a.lower() !=b.lower():
            return False
        min +=1
        max -=1

if __name__=="__main__":
    print isPalindrome('level')
    print isPalindrome('test')

#USING RECURSION

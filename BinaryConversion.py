'''This file contains functions for
converting decimal to binary number'''

#METHOD1
def Dec2Bin(num):
    bStr=""
    while num>0:
        bStr =str(num%2)+bStr
        num=num/2
    return bStr

#METHOD2
def Dec2Bin2(num):
    if num==0:
        return ''
    else:
        return Dec2Bin2(num/2)+str(num%2)
#METHOD3
def Dec2Bin3(num):
    return "{0:#b}".format(num)

'''This program check for duplicate character in
a string'''

def isUniqueChar(str):
    char_set=bytearray(255)
    for x in range(len(str)):
        val=ord(str[x])
        if char_set[val]:
            return False
        char_set[val]=True
    return True

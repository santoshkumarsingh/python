def all_perms(elements):
    '''This function generates all the permutations of
    given inpput'''
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
if __name__=="__main__":
    for x in all_perms('abc'):
        print x
#######OUTPUT#######
#abc
#bac
#bca
#acb
#cab
#cba

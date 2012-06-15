def calculatePi():
    '''This function calculates the value of PI'''
    pi=1
    multiplier=-1
    N_ITERATIONS=500000
    for i in range(3,N_ITERATIONS,2):
        pi +=(1.0/i)*multiplier
        multiplier *=-1
    return pi*4.0

if __name__=="__main__":
    print calculatePi()

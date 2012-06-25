#The game board
import random
board=[0,1,2,
       2,3,4,
       5,6,7]

def show():
    print board[0],'|',board[1],'|',board[2]
    print '__________'
    print board[3],'|',board[4],'|',board[5]
    print '__________'
    print board[6],'|',board[7],'|',board[8]
    print '__________'

while True:
    input=raw_input('Select a spot')
    input=int(input)
    if board[input]!='x' and board[input]!='o':
        
        board[input]='x'
        finding=True
        while finding:
            random.seed()
            opponent=random.randint(0,8)
            if board[opponent]!='o' and board[opponent]!='x':
                board[opponent]='o'
                finding=False
    else:
        print 'spot is taken'
    show()

if __name__=="__main__":
    show()

class Number:
    def __init__(self,value):
        self.value=value
    def execute(self):
        return self.value

class Plus:
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def execute(self):
        return self.left+self.right

class Minus:
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def execute(self):
        return self.left-self.right

class Multiply:
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def execute(self):
        return self.left*self.right
import functools,operator,re
def parser(inp):
    stack=[]
    token_pat = re.compile("\s*(?:(\d+)|(.))")
    for number, op in token_pat.findall(inp):
        if number:
            stack.append(functools.partial(lambda i:i, int(number)))
        else:
            first,second=stack.pop(),stack.pop()
            try:
                op = {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/':operator.div
                }[op]
                print op
            except KeyError:
                raise SyntaxError("unknown operator")

            stack.append(functools.partial(lambda op,first,second:
                        op(first(), second()), op, first, second))
    print(stack[0]())

if __name__=="__main__":
    parser('1 2 + 3 4 * /')
    
            
        
            
    
    
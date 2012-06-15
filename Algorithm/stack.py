class Stack:
        def __init__(self):
                self.items=[]
                self.top=-1
                self.count=0
        def push(self,item):
                
                
                self.items.append(item)
                self.count +=1
        def pop(self):
                if self.top==-1:
                        raise Exception,"Stack is empty"
                else:
                        self.count -=1
                        return items.pop()
        def count(self):
                return self.count
                        

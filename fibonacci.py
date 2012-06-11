class Fib:
    def __init__(self,limit):
        self.limit=limit
        self.a=0
        self.b=1
        self.index=0
    def __iter__(self):
        return self
    def next(self):
        print self.index
        if self.index < self.limit:
            raise StopIteration
        else:
            self.index +=1
            self.a,self.b=self.b,self.a+self.b
            yield self.a

if __name__=="__main__":
    for x in Fib(10):
        print x
        
        
	

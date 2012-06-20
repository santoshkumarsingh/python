'''Implementation of set'''
class Set:
    def __init__(self):
        self._Elements=[]
        self.index=-1
        
    def __len__(self):
        return len(self._Elements)
    
    def __iter__(self):
        return self
    
    def next(self):
        
        if self.index >=len(self._Elements)-1:
            raise StopIteration
        else:
            self.index +=1
            return self._Elements[self.index]
            
            
    def __contains__(self,element):
        return element in self._Elements
    
    def add(self,element):
        if element not in self:
            
            self._Elements.append(element)
            
    def remove(self,element):
        assert element in self,"The element must be in set"
        
        self._Elements.remove(element)
        
    def __eq__(self,setB):
        if len(self)!=len(setB):
            return False
        else:
            self.isSubsetOF(setB)
            
    def isSubsetOf(self,setB):
        for e in self:
            if e not in setB:
                return False
        return True
    def union(self,setB):
        newSet=Set()
        newSet._Elements.extend(self._Elements)
        for e in SetB:
            if e not in self:
                newSet._Elements.append(e)
        return newSet
    

if __name__=="__main__":
    s=Set()
    s.add(2)
    s.add(2)
    s.add(3)
    s.add(4)
    s.add(3)
    
    for x in s:
        print x
        

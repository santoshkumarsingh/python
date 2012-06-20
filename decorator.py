'''Decorators allow you to inject or modify code in functions or
classes.
Suppose  you would like to do something at the entry and exit points of function
such as pefrom some kind of security,tracing,locking etc..'''

class decorator(object):
    def __init__(self,fn):
        self.fn=fn
    def __call__(self,*args,**kwargs):
        print "Start",self.fn.__name__
        ret=self.fn(*args,**kwargs)
        print "Stop",self.fn.__name__
        return ret

'''Test above decorator'''
@decorator
def fun_args(*args):
    print len(args)
    return sum(args)

fun_args(1,2,3,4)




class MethodLogging(type):
    def __new__(mcs,name,bases,dict):
        def log(name,mth):
            def _method(self,*args,**kwargs):
                print "called",name
                return mth(self,*args,**kwargs)
            return _method
        for attr,method in dict.items():
            if callable(method) and not attr.startswith("__"):
                print "Logging",attr
                dict[attr]=log(attr,method)
            return type.__new__(mcs,name,bases,dict)

class Foo(object):
    __metaclass__=MethodLogging
    def a(self):
        print "Hello"
    def b(self,*args):
        print sum(args)
'''Test the Logging method'''
x=Foo()
x.a()
        

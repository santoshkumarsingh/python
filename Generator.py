'''Generators give you lazy evaluation. You use them by iterating over them,
either explicitly with 'for' or implicitly by passing it to any function or
construct that iterates. You can think of generators as returning multiple
items, as if they return a list, but instead of returning them all at once
they return them one-by-one, and the generator function is paused until the
next item is requested.
SOURCE:http://stackoverflow.com/questions/102535/what-can-you-use-python-generator-functions-for
'''
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
    
if __name__=="__main__":
    for c in reverse('cat'):
        print c

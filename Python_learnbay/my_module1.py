def temp_converter(T):
    '''This function is used to convert temp from cel to far'''
    return ((9/5)*T)+32

def even_odd(a):
    '''this will give the odd and even number'''
    even=[]
    if a%2==0:
        return 'even'
    else:
        return 'odd'
if __name__=='__main__':
    print(temp_converter(32))
    print(even_odd(23))
else:
    print("hello world")
    
    
if __name__=='__main__':
    if temp_converter(32)==83:
        print("the function is correct")
    else:
        print("the code is wrong")
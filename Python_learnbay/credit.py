def credit_above_limit(T):
    '''This function is used to convert temp from cel to far'''
    return ((9/5)*T)+32

def credit_below_limit(a):
    '''this will give the odd and even number'''
    even=[]
    if a%2==0:
        return 'even'
    else:
        return 'odd'
if __name__=='__main__':
    print(credit_above_limit(32))
    print(credit_below_limit(23))
else:
    print("hello world")
    
    

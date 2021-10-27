def ad(a, b):
    return(a+b)

def sub(a,b):
    return(a-b)

def multi(a,b):
    return(a*b)

def division(a,b):
    return(a/b)

def increment(a):
    return(a+1)

def decrement(a):
    return(a-1)

print('10', '+', '12', ' = ', ad(10,12))
print('58', '-', '34', ' = ', sub(58,34))
print('6', 'x', '7', ' = ', multi(6,7))
print('144', ':', '12', ' = ', int(division(144,12)))
print('12', '+', '1', ' = ', increment(12))
print('34', '-', '1', ' = ', decrement(34))
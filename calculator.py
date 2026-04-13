# First example
import math
def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    if a == 0:
        raise ZeroDivisionError("Divide by zero error")
    return b / a 

def log(a, b): 
    if a<= 1 or a == 1:
        raise ValueError("Logarithmic error, base must be greater than 1")
    if b<=0:
        raise ValueError("Logarithmic error, must be greater than 0")
    
    return math.log(b,a)

def exp(a, b): 
    return math.pow(a,b)

    


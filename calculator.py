#https://github.com/Phoenixx1st/lab11-AH-CC.git
# Partner 1: Aaron Robertson
# Partner 2: Camila Cabello
import math

# Calculator functions
def square_root(a):
    if a < 0:
        raise ValueError("Square root error, a must be positive")
    return math.sqrt(a)

def hypotenuse(a, b):
        return math.hypot(a, b)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Divide by zero error")
    return b / a

def logarithm(a, b):
    if a<= 0 or a == 1:
        raise ValueError("Logarithmic error, base must be greater than 1")
    if b <= 0:
        raise ValueError("Logarithmic error, must be greater than 0")
    return math.log(b, a)

def exp(a, b):
    return math.pow(a,b)



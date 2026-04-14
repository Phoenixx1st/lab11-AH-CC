import math
def add(a, b):

# Calculator functions
def square_root(a):
    try:
        if a < 0:
            raise ValueError("Square root error, a must be positive")
        return math.sqrt(a)
    except Exception as e:
        return f"Error: {e}"

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        return f"Error: {e}"


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



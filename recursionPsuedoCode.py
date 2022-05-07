"""
def recursionMethod(parameters):
    if exit from condition satisfied:
        return some value
    else:
        recursionMethod(modified parameters)
"""

def firstMethod():
    secondMethod()
    print("I am firstMethod")

def secondMethod():
    thirdMethod()
    print("I am secondMethod")

def thirdMethod():
    fourthMethod()
    print("I am thirdMethod")

def fourthMethod():
    print("I am fourthMethod")


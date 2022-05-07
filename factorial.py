
import sys

def factorial(n):

    if n < 0 or int(n) != n:
        return "Invalid Input"

    if n in [0,1]:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(800))
# print(sys.getrecursionlimit())
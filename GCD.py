
def gcd(a, b):

    if int(a) != a or int(b) != b:
        return "Invalid Input"

    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(48,18))
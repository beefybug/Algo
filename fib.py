import sys

def Mul(m, n):
    """Multiplies 2x2 matrices. Assumes m and n are array of size 4.
    [0, 1   becomes [ 0, 1, 2, 3]
     2, 3]
    """
    R = [0, 0, 0, 0]
    R[0] = m[0]*n[0] + m[1]*n[2]
    R[1] = m[0]*n[1] + m[1]*n[3]
    R[2] = m[2]*n[0] + m[3]*n[2]
    R[3] = m[2]*n[1] + m[3]*n[3]
    return R


def Power(m, p):
    """Calculates the p power of a matrix m.
    Uses the p/2 trick to be O(logn) complexity
    """
    if p <= 1:
        return m
    if p % 2 == 1:
        return Mul(m, Power(m, p-1))
    if p % 2 == 0:
        temp = Power(m, p/2)
        return Mul(temp, temp)


def fib(n):
    """Determines the n-th fibonacci number"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    m = [1, 1, 1, 0]  # Flatten matrix
    R = Power(m, n-1)
    return R[0]


def main():
    for i in range(int(sys.argv[1])):
        print(fib(i))

main()

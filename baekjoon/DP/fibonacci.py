import sys

def fibonacci(n):
    D = [0 for i in range(n+1)]
    D[1] = 1
    for i in range(n+1):
        if i >= 2:
            D[i] = D[i-1] + D[i-2]
    return D[n]

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    res = fibonacci(n)
    sys.stdout.write(str(res))
import sys

def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n

def sum_2(n):
    res = 0
    for i in range(n):
        res += (i+1)
    return res

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    res = sum(n)
    sys.stdout.write(str(res))
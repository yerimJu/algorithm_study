T = int(input())
for i in range(0,T):
    n = int(input())
    a = input().split(' ')
    b = input().split(' ')
    a.sort()
    b.sort()
    if a == b: print('NOT CHEATER')
    else: print('CHEATER')
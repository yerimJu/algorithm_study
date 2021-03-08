# 11053 가장 긴 증가하는 부분 수열 (LIS, Longest Increasing Sub-sequence)

import sys

# 완전 탐색 : O(2^n)
def lis_brute_force(arr):
    n = len(arr)
    if n == 0:
        return 0

    ret = 0
    for i in range(n):
        S = []
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                S.append(arr[j])
        ret = max(ret, 1 + lis_brute_force(S))
    
    return ret

# DP memozation 기법 : O(n^2)
cache = [-1] * 1000
# start에서 시작하는 최대 수열 중 최대 길이를 return
def lis_dp(arr, start):
    ret = cache[start]
    if ret != -1:
        return ret
        
    ret = 1
    n = len(arr)
    for i in range(start+1, n):
        if arr[start] < arr[i]:
            ret = max(ret, 1 + lis_dp(arr, i))
    cache[start] = ret

    return ret

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    # res = lis_brute_force(A)
    
    res = -1
    for i in range(len(A)):
        res = max(res, lis_dp(A, i))

    sys.stdout.write(str(res))
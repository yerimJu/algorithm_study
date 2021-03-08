# 11055 합이 가장 큰 증가 부분 수열 (LIS, Longest Increasing Sub-sequence)

import sys

# DP memozation 기법 : O(n^2)
cache = [-1] * 1000
# start에서 시작하는 최대 수열 중 최대 길이를 return
def lis_sum_dp(arr, start):
    ret = cache[start]
    if ret != -1:
        return ret
        
    ret = arr[start]
    n = len(arr)
    for i in range(start+1, n):
        if arr[start] < arr[i]:
            ret = max(ret, arr[start] + lis_sum_dp(arr, i))
    cache[start] = ret

    return ret

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    res = -1
    for i in range(len(A)):
        res = max(res, lis_sum_dp(A, i))

    sys.stdout.write(str(res))
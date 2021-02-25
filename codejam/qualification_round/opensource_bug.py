import sys
from itertools import combinations


# exception

def calculate_sum_max(values, links):
    # print('values', values)
    # print('links', links)
    result = 0
    # calculate combination in values
    for rr in range(len(values)+1):
        candidates = list(range(len(values)))
        if rr == 0:
            continue

        for ii in range(len(links)):
            if (rr == 1 and values[ii] < 0) or len(links[ii]) >= rr:
                candidates.remove(ii)

        combs = list(combinations(candidates, rr))
        # find the combination by dependency
        for comb in combs:
            flag = True
            temp_sum = 0

            for idx in comb:
                temp_sum += values[idx]
                for jdx in range(len(links[idx])):
                    if links[idx][jdx] not in comb:
                        flag = False
                        break
                if flag == False:
                    break
            if flag == False or temp_sum < 0:
                continue
            # print('comb', comb)

            result = max(result, temp_sum)
                
    return result

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        values = list(map(int, sys.stdin.readline().split()))
        links = []
        for _ in range(n):
            temp = list(map(lambda x: int(x)-1, sys.stdin.readline().split()[1:]))
            links.append(temp)
        # print(links)
        result = calculate_sum_max(values, links)
        # print("="*10)
        print(result)


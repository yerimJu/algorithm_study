import sys

# brute-force
def tsp(path, visit, current_cost):
    # base case
    if len(path) == n:
        total_cost = current_cost + dist[path[-1]][path[0]]
        # print(path, total_cost)
        return total_cost
    
    ret = sys.maxsize
    for i in range(n):
        if visit[i]:
            continue
        curr = path[-1]
        next = i
        path.append(next)
        visit[next] = True
        ret = min(ret, tsp(path, visit, current_cost + dist[curr][next]))
        path.remove(next)
        visit[next] = False
    return ret

if __name__ == '__main__':
    global n
    global dist
    n = int(sys.stdin.readline())
    dist = [[None for j in range(n)] for i in range(n)]
    for i in range(n):
        dist[i] = list(map(int, sys.stdin.readline().split()))
    # print(dist)

    # start with 0th city
    visit = [False for i in range(n)]
    res = sys.maxsize
    for i in range(n):
        path = [i]
        visit[i] = True
        res = min(res, tsp(path, visit, 0))
        visit[i] = False
    sys.stdout.write(str(res))
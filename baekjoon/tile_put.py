import sys

def tile_put():
    return

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    tile = [[0 for col in range(m)] for row in range(n)]
    for i in range(n):
        c = sys.stdin.readline()
        for j in range(m):
            if c[j] == '.':
                tile[i][j] = 1
            elif c[j] == '*':
                tile[i][j] = 0
    
    # for i in range(n):
    #     print(tile[i])
    
    tile_put()
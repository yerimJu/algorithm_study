from itertools import combinations
from itertools import permutations

items = ['a', 'b', 'c', 'd']

print(len(items))

# Result:
# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]
print(list(permutations(items, 2)))

# Result:
# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
print(list(combinations(items, 2)))
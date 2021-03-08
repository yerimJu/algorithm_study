### 2019 SEED

# Python의 강점
1. Integer limit이 없다.
2. 글자 n번 출력하기
    ```python
    print(n*'=')
    ```
3. Permutation, combination 함수가 제공된다.
    ```python
    from itertools import permutations
    from itertools import combination
    ```
4. List, String에서 slicing이 유용하다.
5. for-else 구문 (for문에 한 번도 걸리지 않을 때)
    ```python
    for i in data:
        if i > 10:
            break
    else:
        print('All items are lower than 10.')
    ```
6. Multiple return values
    ```python
    return a, b, c
    ```
7. Chained comparision
    ```python
    if a < b < c:
    ```
8. Swapping variables
    ```python
    x, y = y, x
    ```
9. 유용한 내장 함수 : map
    ```python
    map(변환 함수, 순회 가능한 데이터)

    # list의 특정 요소에 lambda식을 적용하여 순회 및 출력
    users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'}
    for sex_kor in map(lambda u: "남" if u["sex"] == "M" else "여", users):
        print(sex_kor)
    ```
10. 유용한 내장 함수 : reduce
    ```python
    reduce(집계 함수, 순회 가능한 데이터[, 초기값])
    
    from functools import reduce
    users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'}
    # 나이 합계
    reduce(lambda acc, cur: acc + cur["age"], users, 0)
    # 이메일 목록
    reduce(lambda acc, cur: acc + [cur["mail"]], users, [])
    ```
11. 자료 구조가 다양하고 변환이 쉬움 : List, Set, Dictionary
    ```python
    a = []
    a = list()
    b = set()
    c = {}
    c = dict()
    ```
12. Tips
    ```python
    # 입출력
    import sys
    input = sys.stdin.read().split()

    # test할 때
    import sys
    sys.stdin = open('input.in', 'r')
    sys.stdout = open('output.out', 'w')

    # 프로그램 종료
    import sys
    sys.exit()

    # 2차원 list 초기화 (N*M)
    arr = [[0 for col in range(M))] for row in range(N)]

    # sorted를 이용한 정렬
    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]
    sorted(student_tuples, key=lambda student: student[2]) # sort by age

    # Stack
    stack = []
    stack.append(1)
    stack.append(2)
    stack.pop() # 2

    # Queue (Double )
    from collections import deque
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.popleft() # 1

    # pow식
    x^y mod p = pow(x, y, p)
    ```
13. Compiler는 Python3보다 Pypy3가 빠르다.
14. 마이너스 배열 1*1000 초기화
    ```python
    import math
    arr = [-math.inf] * 1000
    ```
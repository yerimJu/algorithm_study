# 2021_2_C

from abc import abstractproperty
import sys
from itertools import combinations


T = int(sys.stdin.readline())

for test_case in range(T):
    # map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다
    n, x = map(int, sys.stdin.readline().split(' '))

    card_list = [i+1 for i in range(n)]
    # print(card_list)

    # make combination list
    comb_list = []
    if n % 2 == 0:
        comb_list = list(combinations(card_list, int(n/2)))
    else:
        comb_list = list(combinations(card_list, int(n/2)+1))
    # print(comb_list)

    # compare 점화식
    comb_success = []
    flag = False
    for comb in comb_list:
        comb_list.remove(comb)
        sub_sum = sum(comb)
        total_sum = sum(card_list)

        if sub_sum == (total_sum + x)/2:
            # print array
            alice_cards = list(comb)
            bob_cards = [card for card in card_list if card not in alice_cards]
            # print(alice_cards)
            # print(bob_cards)

            while len(alice_cards) > 0:
                # print('alice: {0}'.format(alice_cards))
                # print('bob: {0}'.format(bob_cards))

                comb_success.append(alice_cards.pop())
                if len(bob_cards) > 0: comb_success.append(bob_cards.pop())
            flag = True
            break
        else:
            continue
    
    if flag:
        print('YES')
        # * symbol is use to print the list elements in a single line with space.
        print(*comb_success)
    else:
        print('NO')

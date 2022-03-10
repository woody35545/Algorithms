# -*- coding: utf-8 -*- 
"""
--- BOJ_2869 ---

[문제]
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

[출력] 
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

[예제 입력] 
2 1 5

[예제 출력]
4

"""
#===#
# [] 2020.03.10: 정상적으로 작동하기는 하는데, 값이 커지면 시간초과 발생. 알고리즘 바꾸어야 함.
# [] 2020.03.10: 어떤 알고리즘 사용하는게 효율적일지 찾아보기
#===#


# A = 달팽이가 낮에 올라갈 수 있는 거리
# B = 밤에 자는 동안 미끄러지는 거리
# V = 달팽이가 올라야하는 막대의 높이

A,B,V = [int(x) for x in input().split(" ")]

def solve():
    day_required = 1  # 달팽이가 오르는데 걸리는 일수, 0으로 초기화
    target_height = V # 달팽이가 도달해야 하는 위치
    current_height = 0 # 달팽이 현재 위치
    move = A # 달팽이가 낮에 움직이는 거리
    sleep = B # 달팽이가 잘 때 떨어지는 거리

    while(True):
        current_height += move
        if(current_height >= target_height):
            # 낮에 올라간걸로 도달하면 밤을 보내지 않고 break    
            break
        else:

            # 낮에 올라간걸로 부족하다면 잠을 잔 후 다음날 다시 오름
            current_height -= sleep # 자는동안 일정높이 떨어지므로.
            day_required += 1 # 잠을 잔 이후에 하루 추가되므로 +1
            
    print(day_required)

solve()

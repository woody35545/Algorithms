# -*- coding: utf-8 -*-

"""
--- BOJ_17952---
[문제]
성애는 이번 학기에 전공을 정말 많이 듣는다. 이로 인해 거의 매일을 과제를 하면서 보내고 있다. 그런데도 과제가 줄어들 기미가 보이지 않는데, 바로 분단위로 과제가 추가되고 있기 때문이다. 다행히 과제 제출 기한은 학기가 끝날 때까지이다. 너무나도 많은 과제를 하다가 미쳐버린 성애는 아래와 같은 규칙으로 과제를 해 나가고 있다.

과제는 가장 최근에 나온 순서대로 한다. 또한 과제를 받으면 바로 시작한다.
과제를 하던 도중 새로운 과제가 나온다면, 하던 과제를 중단하고 새로운 과제를 진행한다.
새로운 과제가 끝났다면, 이전에 하던 과제를 이전에 하던 부분부터 이어서 한다. (성애는 기억력이 좋기 때문에 아무리 긴 시간이 지나도 본인이 하던 부분을 기억할 수 있다.)
성애는 과제를 받자마자 이 과제가 몇 분이 걸릴지 정확하게 알 수 있고, 성애가 제출한 과제는 무조건 만점을 받는다.

성애는 이번 학기에 자기가 받을 과제 점수를 예상해보고 싶다. 하지만 과제 점수를 예상하는 지금도 과제가 추가되고 있기에 여유를 부릴 수가 없다. 여러분이 성애가 받을 과제 점수를 구해주자!

[입력]
첫째 줄에 이번 학기가 몇 분인지를 나타내는 정수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

두번째 줄부터 N줄 동안은 학기가 시작하고 N분째에 주어진 과제의 정보가 아래의 두 경우 중 하나로 주어진다.

1 A T: 과제의 만점은 A점이고, 성애가 이 과제를 해결하는데 T분이 걸린다. A와 T는 모두 정수이다. (1 ≤ A ≤ 100, 1 ≤ T ≤ 1,000,000)
0: 해당 시점에는 과제가 주어지지 않았다.

[출력]
성애가 받을 과제 점수를 출력한다.

[에제입력]
---------
3
1 100 3
0
0
---------
설명:
1분째: 100점짜리 과제 1이 주어지고 이 과제를 하는데 3분이 걸린다. 과제를 받자마자 시작했으므로 과제 1이 끝나는데는 이제 2분 남았다.
2분째: 새로운 과제가 주어지지 않았으므로 과제 1을 이어서 한다.
3분째: 새로운 과제가 주어지지 않았으므로 과제 1을 이어서 한다. 이 시점에 과제 1이 끝나서 100점을 획득한다.

[예제출력]
100

"""


# 과제의 순서는 Stack으로 관리
# 과제 진행 시간을 가지고 있기 위해서 남은 얼마나 더해야하는지 기록하는 remaining_time : list 선언 


def solve():
    # N = 이번학기 시간
    N = int(input())
    todo = [0] * N  # 과제들
    remaining = [0] * N  # 과제 완료까지 남은시간
    scores = [0] * N  # 과제당 점수
    total_score = 0  # 총 취득 점수
    current = 0  # 현재 진행중인 과제 번호
    stack = [0] * N
    size_of_stack = 0
    last_added_project = 0
    number_of_projects = 0
    for n in range(N):
        input_str = input().split(" ")
        if (int(input_str[0]) == 0):
            None
        else:
            stack[size_of_stack] = last_added_project

            last_added_project += 1
            size_of_stack += 1

            scores[last_added_project] = int(input_str[1])
            remaining[last_added_project] = int(input_str[2])
            number_of_projects += 1
            current = last_added_project

        remaining[current] -= remaining[current - 1]

        if (n == N - 1):
            for i in range(number_of_projects):
                if (remaining[i] == 0):
                    total_score += scores[i]

    print(total_score)


solve()

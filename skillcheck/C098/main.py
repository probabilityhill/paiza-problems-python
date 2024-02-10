N = int(input())
ball_num_dict = {}
# 最初に持っているボールの数を記録
for i in range(1, N + 1):
    ball_num_dict[i] = int(input())
    
M = int(input())
for _ in range(M):
    person_from, person_to, ball_num = map(int, input().split())
    # パスされるボールの数  
    ball_num_passed = min(ball_num, ball_num_dict[person_from])
    # ボールをパスする
    ball_num_dict[person_from] -= ball_num_passed
    ball_num_dict[person_to] += ball_num_passed

# 最終的なボールの数を出力する
print(*list(ball_num_dict.values()), sep='\n')

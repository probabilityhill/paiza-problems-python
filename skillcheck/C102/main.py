DAYS_PER_MONTH = 31
A_LIVE = 'A'
B_LIVE = 'B'
NO_LIVE = 'x'
schedule = [NO_LIVE] * DAYS_PER_MONTH

a_live_num = int(input())
for _ in range(a_live_num):
    day = int(input())
    schedule[day - 1] = A_LIVE

b_live_num = int(input())
is_b_next = False
for _ in range(b_live_num):
    day = int(input())
    # Aのライブがある場合はAとB交互になるように選ぶ
    if schedule[day - 1] == A_LIVE:
        if is_b_next:
            schedule[day - 1] = B_LIVE
        is_b_next = not is_b_next
    else:
        schedule[day - 1] = B_LIVE

print(*schedule, sep='\n')

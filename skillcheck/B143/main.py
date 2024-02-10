N, rps_num = map(int, input().split())
# index: 先頭の園児の出席番号 - 1, value: 列の長さ
cols = [1] * N

for _ in range(rps_num):
    winner, loser = map(int, input().split())
    # 勝者の列の後ろに敗者の列が連結する
    cols[winner - 1] += cols[loser - 1]
    # 敗者は先頭でなくなる
    cols[loser - 1] = 0
# 最長の列の長さ
max_col = max(cols)
# 最長の列の先頭の園児の出席番号を出力
result = ''
for i in range(N):
    if cols[i] == max_col:
        result += str(i + 1) + '\n'
print(result)

N = int(input())
products = [False] * N
# N番までの製品の中で届いたものを記録する
for _ in range(N):
    no = int(input())
    if no - 1 < N:
        products[no - 1] = True
# 届いていない製品の数
not_exists_num = len(list(filter(lambda x: not x, products)))
print(not_exists_num)

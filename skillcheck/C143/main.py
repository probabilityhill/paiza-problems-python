import re

s = input()
# 長さ2以上のハイフンを長さ1のハイフンにする
result = re.sub('-+', '-', s)
print(result)

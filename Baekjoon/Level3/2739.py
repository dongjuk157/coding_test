# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
# 출력형식과 같게 N*1부터 N*9까지 출력한다.

N = int(input())

for i in range(1, 10):
    print(f"{N} * {i} = {N * i}")
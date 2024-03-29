import math
N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
left, right = max(arr), sum(arr)

while left <= right:
    mid = (left + right) // 2

    count, sum = 0, 0
    for i in range(N):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]
    if sum:
        count += 1

    # print("left: ", left, "right: ", right, "mid: ", mid, "count: ", count)

    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)
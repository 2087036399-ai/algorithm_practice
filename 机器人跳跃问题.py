# 机器人跳跃问题：https://www.nowcoder.com/practice/7037a3d57bbd4336856b8e16a9cafd71
# 主要是利用二分答案来解决 因为初始值越大 越容易跳过；具有单调性

ans = 0
n = int(input())
a = list(map(int, input().split()))
l = 0
r = max(a)
maxn = max(a)

def f(mid: int) -> bool:
    sum = mid
    for num in a:
        if sum <= num:
            sum -= (num - sum)
        else:
            sum += (sum - num)
        if (sum >= maxn):
            return True
        if (sum < 0):
            return False
    return True


while l <= r:
    mid = (l + r) // 2
    if f(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)

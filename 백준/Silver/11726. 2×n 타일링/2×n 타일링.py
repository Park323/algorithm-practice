n = int(input())

# def fibo(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return fibo(n-1) + fibo(n-2)

# print(fibo(n))

dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i < 3:
        dp[i] = i
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)
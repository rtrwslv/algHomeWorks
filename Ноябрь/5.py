#O(n - 1)
prices = [3, 2, 1, 4]
n = len(prices)
dp = [1] * n
for i in range(1, n):
	if prices[i] + 1 == prices[i-1]:
		dp[i] += dp[i-1]
print(sum(dp))

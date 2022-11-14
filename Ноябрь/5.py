
prices = [8, 6, 7, 7]
result = len(prices)
for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        if prices[i] - prices[j] == 1:
            print(prices[i], prices[j])
            result += 1
print(result)
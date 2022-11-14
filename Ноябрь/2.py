n = 7
result = [0, 1]
i = 1
if n >= 2:
    result = result + [0] * (n-1)
    while (i * 2) + 1 < n + 2:
        if i % 2 != 0:
            result[i * 2] = result[i]
            if i * 2 < n:
                result[i * 2 + 1] = result[i] + result[i + 1]
            i += 1
        else:
            result[i * 2 + 1] = result[i] + result[i + 1]
            result[i * 2] = result[i]
            i += 1
print(max(result))

max = 0
values = [8,1,5,2,6]
for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] + values[j] + i - j > max:
            max = values[i] + values[j] + i - j
print(max)
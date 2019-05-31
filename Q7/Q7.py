number_array = list(map(int, input().split()))
print(*[number_array[i] for i in range(0, len(number_array)) if((i+1) % 6 == 0) & (number_array[i] % 6 == 0)])

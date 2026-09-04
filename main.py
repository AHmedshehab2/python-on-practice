def average(*nums):
    return sum(nums) / len(nums)


n = int(input().strip())

numbers = []
while len(numbers) < n:
    line_values = [float(x) for x in input().split()]
    numbers.extend(line_values)

result = average(*numbers)
print(f"{result:.2f}")
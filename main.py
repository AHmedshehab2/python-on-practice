n = int(input())
nums = [int(input()) for _ in range(n)]
# Find and print the second largest unique value
nums.sort(reverse=True)
unique_nums = list(set(nums))
print(unique_nums[1] if len(unique_nums) > 2 else unique_nums[0])

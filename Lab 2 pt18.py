#Part 18 Replacing items in list
nums = [100, 200, 300, 400, 500]
print(nums) #to show original list
for i in range(len(nums)):
    nums[i] = [100, 300, 500, 700, 900][i]

print(nums)
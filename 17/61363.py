nums = list(map(int, open('61363.txt').readlines()))
a = len(nums)
m = 0
k = 0
l = 0
for x in nums:
    if x % 100 == 19:
        k = max(k, x)
for i in range(0, a - 2):
    if (len(str(nums[i])) == 4 and len(str(nums[i + 1])) == 4 and len(str(nums[i + 2])) != 4) or (
            len(str(nums[i])) == 4 and len(str(nums[i + 1])) != 4 and len(str(nums[i + 2])) == 4) or (
            len(str(nums[i])) != 4 and len(str(nums[i + 1])) == 4 and len(str(nums[i + 2])) == 4):
        if nums[i] % 3 == 0 or nums[i + 1] % 3 == 0 or nums[i + 2] % 3 == 0:
            if nums[i] + nums[i + 1] + nums[i + 2] > k:
                m += 1
                l = max(nums[i] + nums[i + 1] + nums[i + 2], l)
print(m, l)

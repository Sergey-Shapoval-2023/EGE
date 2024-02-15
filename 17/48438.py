# map(функция, список) - применяет функцию к каждому элементу списка
nums = list(map(int, open('48438.txt').readlines()))

min_num = 10001
for num in nums:
    if abs(num) % 10 == 7:
        min_num = min(min_num, num)

"""
a b xor
0 0 0
0 1 1
1 0 1
1 1 0
"""
count = 0
max_sum = 0
for i in range(len(nums) - 1):
    # xor заменяется на != 
    if (abs(nums[i]) % 10 == 7) != (abs(nums[i + 1]) % 10 == 7) and (nums[i] ** 2 + nums[i + 1] ** 2 < min_num ** 2):
         count += 1
         max_sum = max(max_sum, nums[i] ** 2 + nums[i + 1] ** 2)

print(count, max_sum)

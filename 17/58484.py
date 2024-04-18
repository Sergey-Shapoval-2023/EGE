nums = list(map(int,open('/Users/sergejsapoval/Downloads/58584.txt').readlines()))
a = len(nums)
count = 0
s = 0
min_num = 20000
for x in nums:
    if len(str(x))==3 and x%10==5 and  x < min_num:
        min_num = x


for i in range(0,a-1):



    if (len(str(nums[i])))==4 + (len(str(nums[i+1])))==4:
        count+=1










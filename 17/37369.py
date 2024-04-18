nums = list(map(int,open('/Users/sergejsapoval/Downloads/17-5.txt').readlines()))
a = len(nums)
count = 0
s = 0
for i in range(0,a-1):
    for x in range(i+1,a):
        if (nums[i]-nums[x])%80==0:
         count+=1
         s = max(s,nums[i]-nums[x])
print(count,s)


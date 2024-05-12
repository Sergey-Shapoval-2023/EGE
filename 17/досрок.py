nums = list(map(int,open('/Users/sergejsapoval/Downloads/17-10.txt')))
a = len(nums)
count = 0
k = 0
b = 0
for x in nums:
    if x %19==0:
        k = max(k,x)
for i in range(a-1):
    if nums[i]>k or   nums[i+1] > k:
        count+=1
        b = max(b,nums[i]+ nums[i+1])
print(count,b)






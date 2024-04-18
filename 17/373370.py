nums = list(map(int,open('/Users/sergejsapoval/Downloads/17-6.txt')))
a = len(nums)
count = 0
s = 0
for i in range(0,a-1):
    for x in range(i+1,a):
        if (nums[i]-nums[x])%60==0 and (nums[i]%15==0 or nums[x]%15==0):
            count+=1
            s = max(s,nums[i]-nums[x])
print(count,s)

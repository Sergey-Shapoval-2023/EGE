nums = list(map(int, open('/Users/sergejsapoval/Downloads/17-2.txt').readlines()))
a = len(nums)
count = 0
s = 0
for i in range(0,a-1):
    if nums[i] * nums[i+1]%15==0 and (nums[i] + nums[i+1])%7==0:
        count+=1
        s = max(s,nums[i] + nums[i + 1])
print(count,s)




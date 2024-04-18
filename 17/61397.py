nums = list(map(int,open('/Users/sergejsapoval/Downloads/17-7.txt')))
a = len(nums)
count = 0
s = 0
b = 0
for i in range(0,a):
    if nums[i]%100==17:
        s = max(s,nums[i])
for i in range(0,a-2):
    if int(len(str(nums[i]))==4) + int(len(str(nums[i+1]))==4) + int(len(str(nums[i+2]))==4)==2:
        if nums[i]%5==0 or nums[i+1]%5==0 or nums[i+2]%5==0:
            if nums[i] + nums[i+1] +nums[i+2] > s:
                count+=1
                b = max(b,nums[i] + nums[i+1] +nums[i+2])

print (count, b)




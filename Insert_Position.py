nums = [1,3,5,6]
target = 2
indexOfTarget=None
if target in nums:
    indexOfTarget = nums.index(target)
else :
    nums.append(target)
    nums.sort()
    indexOfTarget=nums.index(target)

print(indexOfTarget)

def twoSum(nums, target):
    lookup = {}
    for i in range(len(nums)):
        if nums[i] in lookup:
            return [lookup[nums[i]], i]
        else:
            lookup[target-nums[i]] = i

    return None

print(twoSum([2,7,11,15], 23))



def test(nums):
    return len(nums) == 8 and nums.count(nums[4])==3

nums=[19,19,15,5,5,5,1,2]
nums1=[19,15,5,7,5,5,2]
nums2=[11,12,14,13,14,13,15,14]
nums3=[19,15,11,7,5,6,2]
print(test(nums))
print(test(nums1))
print(test(nums2))
print(test(nums3))
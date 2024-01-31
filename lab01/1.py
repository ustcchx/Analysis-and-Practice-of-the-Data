class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenth=len(nums)
        for i in range(lenth)[:lenth-1]:
            for j in range(lenth)[i+1:]:
                if nums[i]+nums[j] == target :
                    return [i,j]
        
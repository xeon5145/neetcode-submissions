class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sumList = {};

        # for i,num in enumerate(nums):
        #     diff = target - num

        #     if diff in sumList:
        #         return [sumList[diff],i ]

        #     sumList[num] = i

        # return sumList;

        # Better One
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i + 1:]:
                j = nums.index(diff, i + 1)
                return [i, j]

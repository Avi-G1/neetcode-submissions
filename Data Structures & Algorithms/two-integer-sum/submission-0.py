class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if (needed in dictt):
                return [dictt[needed], i]
            else:
                dictt[nums[i]] = i

        return Null

        

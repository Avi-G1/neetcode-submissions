class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        zeroCount = 0
        
        for x in nums:
            if (x == 0):
                zeroCount += 1
                continue
            result *= x

        output = []

        for val in nums:
            if zeroCount > 1:
                output.append(0)
            elif zeroCount == 1:
                if (val == 0):
                    output.append(result)
                else:
                    output.append(0)
            else:
                output.append(int(result / val))

        return output

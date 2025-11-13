# https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  # XOR cancels out duplicate numbers
        return result
        
if __name__ == "__main__":
    print(Solution().singleNumber([2,2,1]))
    print(Solution().singleNumber([4,1,2,1,2]))
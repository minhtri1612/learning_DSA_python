# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def maxSubArray(self, nums):
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0
            
            total += n
            res = max(res, total)
        
        return res
if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
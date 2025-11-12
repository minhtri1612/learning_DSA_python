# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
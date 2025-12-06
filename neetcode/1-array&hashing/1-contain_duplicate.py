# https://leetcode.com/problems/contains-duplicate/description/


class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums) - 1):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

if __name__ == "__main__":
    print(Solution().containsDuplicate([1, 2, 3, 1]))
    print(Solution().containsDuplicate([1, 2, 3, 4]))
    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 4, 2, 2]))
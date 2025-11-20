#https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
                
if __name__ == "__main__":
    print(Solution().containsDuplicate([1,2,3,1]))
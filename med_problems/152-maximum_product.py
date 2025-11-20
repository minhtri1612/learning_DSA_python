# https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums):
        min_prod = max_prod = ans = nums[0]

        for i in range(1, len(nums)):
            value = nums[i]

            max_temp = max_prod * value
            min_temp = min_prod * value

            min_prod = min(max_temp, min_temp, value)
            max_prod = max(max_temp, min_temp, value)
            ans = max(ans, max_prod)

        return ans


if __name__ == "__main__":
    print(Solution().maxProduct([2,3,-2,4]))
    print(Solution().maxProduct([-2,0,-1]))
    print(Solution().maxProduct([-2,3,-4]))
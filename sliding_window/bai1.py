# 7 -> 3 -> 3 -> 3 -> 2 -> 2 -> 2 -> 2 
# find the length of the longest subarray with the same value in each position

def longest_sub_array(nums: list[int]) -> list[int]:
    left, right = 0, 0
    current_max_length = 0
    count = 0

    while right < len(nums):
        if nums[left] == nums[right]:
            count += 1
            right +=1
        else:
            left = right
            current_max_length = max(current_max_length, count)
            count = 0

    return max(count, current_max_length)
print(longest_sub_array([7,3,3,3,2,2,2,2]))  # EXPECTED OUTPUT: 4
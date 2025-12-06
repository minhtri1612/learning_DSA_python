# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        return s == t
    
if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))
    print(Solution().isAnagram("rat", "car"))
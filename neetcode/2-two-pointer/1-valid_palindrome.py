# https://neetcode.io/problems/is-palindrome/question?list=neetcode150


class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        check_s = "".join(
            char.lower()
            for char in s
            if char.isalnum()
        )
        return check_s == check_s[::-1]
if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))        
    print(Solution().isPalindrome("Was it a car or a cat I saw?"))
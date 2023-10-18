class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)  # Convert x to a string
        for i in range(len(x_str) // 2):  # Only need to iterate half the string length
            if x_str[i] != x_str[-i - 1]:  # Compare characters at corresponding positions
                return False  # Return False as soon as a mismatch is found
        return True  # If the loop completes, the number is a palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for c in s:
            if c.isalnum(): #keep only alpha numeric 
                newS += c.lower() #cause its case-insensitive 
        return newS == newS[::-1]

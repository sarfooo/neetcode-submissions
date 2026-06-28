class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = []
        for char in s:
            chars.append(char)

        for char in t:
            if char in chars:
                chars.remove(char)

        return len(chars) == 0